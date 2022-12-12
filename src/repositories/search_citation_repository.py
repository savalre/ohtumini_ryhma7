"""
SearchCitationRepository
Handles the storing and fetching of citations in the DB
Accepts and returns Citation objects
"""
from sqlalchemy.exc import IntegrityError
from db.db import db
from entities.citation import Citation

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
        
    def fetch_citations(self):
        """
        Returns rows of non-deleted citations from DB
        Returns:
            list of tuples
        """

        sql ="""SELECT c.id, e.cite_as, e.type, f.type, f.value
                FROM citations c, entry_types e, fields f
                WHERE c.id=e.citation_id AND c.id=f.citation_id
                AND c.deleted=0 ORDER BY c.id"""


        return self._db.session.execute(sql).fetchall()

    def list_citations(self):
        """
        Returns a list of non-deleted citations
        Returns:
            list of Citation type citations
        """
        fetched_result = self.fetch_citations()
        new_fetched_result = []
        for result in fetched_result:
            if result[0] not in self.group_result:
                self.group_result[result[0]] = []
            
            if result[0] in self.group_result:
                self.group_result[result[0]].append(result[4])

        for citation in self.group_result:
            for citation_field in self.group_result[citation]:
                if self.keyword in citation_field:
                    for field in fetched_result:
                        if field[0] == citation and field not in new_fetched_result:
                            new_fetched_result.append(field)

        fields = []
        citations = []
        # value[0] = c.id
        # value[1] = e.cite_as
        # value[2] = e.type
        # value[3] = f.type
        # value[4] = f.value

        if len(new_fetched_result) > 0:
            citation_id = new_fetched_result[0][0]
        else:
            citation_id = 0

        cite_as = ""
        entry_name = ""

        for value in new_fetched_result:
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
        if len(new_fetched_result) > 0:
            citation = Citation(cite_as, entry_name, fields)
            citations.append(citation)
        return citations