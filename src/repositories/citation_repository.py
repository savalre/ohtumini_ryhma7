"""
CitationRepository
Handles the storing and fetching of citations in the DB
Accepts and returns Citation objects
"""
from sqlalchemy.exc import IntegrityError
from db.db import db
from entities.citation import Citation

class CitationRepository:
    """
    Repository for Citations
    Accepts an SQLAlchemy DB connection as a parameter
    Uses the DB to store and fetch Citations
    """
    def __init__(self, database=db):
        self._db = database

    def store_citation(self, citation):
        """
        Stores the citation in a DB
        Parameters:
            citation of type Citation
        Returns:
            True if succesful, otherwise False
        """
        cite_as = citation.cite_as
        entry_type = citation.entryname
        if not cite_as or not entry_type:
            return False

        self._db.session.begin()
        try:
            sql_citation = "INSERT INTO citations (deleted) \
                    VALUES (0) RETURNING id"
            citation_id = self._db.session.execute(sql_citation).fetchone()[0]

            sql_entry_type = "INSERT INTO entry_types (citation_id, type, cite_as) \
                    VALUES (:citation_id, :entry_type, :cite_as)"
            self._db.session.execute(sql_entry_type, {"citation_id": citation_id,
                                                      "entry_type":entry_type, "cite_as":cite_as})

            sql_field = "INSERT INTO fields (citation_id, type, value)\
                    VALUES (:citation_id, :type, :value)"

            for field_type in citation.fieldtypes:
                self._db.session.execute(sql_field, {"citation_id": citation_id,
                                                     "type":field_type[0], "value" :field_type[1]})
            self._db.session.commit()
            return True
        except IntegrityError as error:
            print(error)
            self._db.session.rollback()
            return False

    def fetch_citations(self):
        """
        Returns rows of non-deleted citations from DB
        Returns:
            list of tuples
        """

        sql = """SELECT c.id, e.cite_as, e.type, f.type, f.value
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

        fields = []
        citations = []
        # value[0] = c.id
        # value[1] = e.cite_as
        # value[2] = e.type
        # value[3] = f.type
        # value[4] = f.value

        if len(fetched_result) > 0:
            citation_id = fetched_result[0][0]
        else:
            citation_id = 0

        cite_as = ""
        entry_name = ""

        for value in fetched_result:
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
        if len(fetched_result) > 0:
            citation = Citation(cite_as, entry_name, fields)
            citations.append(citation)
        return citations

    def clear_citations(self):
        """
        Clears all citation-related tables from DB
        Takes no arguments and returns nothing
        """
        self._db.session.begin()
        sql = "DELETE FROM fields"
        self._db.session.execute(sql)
        sql = "DELETE FROM entry_types"
        self._db.session.execute(sql)
        sql = "DELETE FROM citations"
        self._db.session.execute(sql)
        self._db.session.commit()
    
    def delete_selected_citations(self,deletions_list):
        """
        """
        deleting_citations = deletions_list
        self._db.session.begin()
        for citation in deleting_citations:
            values = {'citation': citation}
            sql = "SELECT c.id FROM citations c, entry_types e WHERE c.id=e.citation_id AND e.cite_as= :citation"
            citation_id = self._db.session.execute(sql,values).one()
            print("SITAATIN ID = ", citation_id[0])
            values = {'id': citation_id[0]}
            sql = "UPDATE citations SET deleted = 1 WHERE id= :id"        
            self._db.session.execute(sql,values)

        #sql = "INSERT INTO "
        #SELECT c.id, e.cite_as, e.type, f.type, f.value
         #       FROM citations c, entry_types e, fields f
          #      WHERE c.id=e.citation_id AND c.id=f.citation_id
           #     AND c.deleted=0 ORDER BY c.id"

        self._db.session.commit()
        return True

default_citation_repository = CitationRepository()
