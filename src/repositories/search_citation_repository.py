"""
SearchCitationRepository
Handles the storing and fetching of citations in the DB
Accepts and returns Citation objects
"""
from sqlalchemy.exc import IntegrityError
from db.db import db
from entities.citation import Citation
from repositories.citation_repository import CitationRepository

class SearchCitationRepository:
    """
    Repository for Citations
    Accepts an SQLAlchemy DB connection as a parameter
    Uses the DB to store and fetch Citations
    """
    def __init__(self, keyword, database=db):
        self.keyword = keyword
        self._db = database
        self.group_result = {}
        self.new_fetched_result = []
        
    
    def group_citations(self, fetched_result):
        """
        Creates a dictionary of citations grouped by id
        Takes in .fetchall() from CitationRepository as a parameter
        Returns:
            Dictionary of citations
        """
        for result in fetched_result:
            if result[0] not in self.group_result:
                self.group_result[result[0]] = []
            
            if result[0] in self.group_result:
                self.group_result[result[0]].append(result[4])
    
    def filter_citations(self, fetched_result):
        """
        Creates a filtered list of citations filtered by self.keyword given by user
        Takes in .fetchall() from CitationRepository as a parameter
        Returns:
            List of filtered citations
        """
        for citation in self.group_result:
            for citation_field in self.group_result[citation]:
                if self.keyword in citation_field:
                    for field in fetched_result:
                        if field[0] == citation and field not in self.new_fetched_result:
                            self.new_fetched_result.append(field)    
    
    def list_citations(self):
        """
        Returns a list of non-deleted citations filtered by keyword in any value field
        Returns:
            list of Citation type citations
        """
        fetched_result = CitationRepository.fetch_citations(self)
        
        self.group_citations(fetched_result)
        self.filter_citations(fetched_result)

        fields = []
        citations = []
        # value[0] = c.id
        # value[1] = e.cite_as
        # value[2] = e.type
        # value[3] = f.type
        # value[4] = f.value

        if len(self.new_fetched_result) > 0:
            citation_id = self.new_fetched_result[0][0]
        else:
            citation_id = 0

        cite_as = ""
        entry_name = ""

        for value in self.new_fetched_result:
            if value[0] > citation_id:
                citation_id = value[0]
                citation = Citation(cite_as, entry_name, fields)
                citations.append(citation)
                fields = []
                cite_as = ""
                entry_name = ""
            fields.append((value[3], value[4]))
            cite_as = value[1]
            entry_name = value[2]

        # Janky way to get the last citation out
        if len(self.new_fetched_result) > 0:
            citation = Citation(cite_as, entry_name, fields)
            citations.append(citation)
        return citations