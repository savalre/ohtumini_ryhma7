"""
CitationRepository
Handles the storing and fetching of citations in the DB
Accepts and returns Citation objects
"""
from sqlalchemy.exc import IntegrityError
from db.db import db

class PlaceholderCitation:
    """
    Placholder for proper citation
    """
    def __init__(self, entry_type, data):
        self.entry_type = entry_type
        self.data = data

    def true(self):
        """
        Returns True
        """
        return True

    def false(self):
        """
        Returns False
        """
        return False

class CitationRepository:
    """
    Repository for Citations
    Accepts an SQLAlchemy DB connection as a parameter
    Uses the DB to store and fetch Citations
    """
    def __init__(self, database=db):
        self._db = database

    def store_citation(self, user_id, citation):
        """
        Stores the citation in a DB
        Parameters:
            user_id to associate the citation with
            citation of type Citation
        Returns:
            True if succesful, otherwise False
        """
        #PLACEHOLDER CODE TO EXTRACT DATA FROM CITATION CLASS
        entry_type = citation.entry_type
        cite_as = "test"
        data = citation.data

        self._db.session.begin()
        try:
            sql_citation = "INSERT INTO citations (user_id, deleted) \
                    VALUES (:user_id, 0) RETURNING id"
            citation_id = self._db.session.execute(sql_citation, {"user_id": user_id}).fetchone()[0]

            sql_entry_type = "INSERT INTO entry_types (citation_id, type, cite_as, deleted) \
                    VALUES (:citation_id, :entry_type, :cite_as, 0)"
            self._db.session.execute(sql_entry_type, {"citation_id": citation_id,
                                                      "entry_type":entry_type, "cite_as":cite_as})

            sql_field = "INSERT INTO fields (citation_id, type, value, deleted)\
                    VALUES (:citation_id, :type, :value, 0)"

            for field_type, value in data.items():
                self._db.session.execute(sql_field, {"citation_id": citation_id,
                                                     "type":field_type, "value" :value})
            self._db.session.commit()
            return True
        except IntegrityError as error:
            print(error)
            self._db.session.rollback()
            return False

    def list_citations(self, user_id):
        """
        Returns a list of non-deleted citations by user id
        Returns:
            list of Citation type citations
        """
        sql = "SELECT c.id, e.cite_as, e.type, f.type, f.value \
                FROM citations c, entry_types e, fields f \
                WHERE c.user_id=:user_id AND c.id=e.citation_id AND c.id=f.citation_id \
                AND c.deleted=0 ORDER BY c.id"

        result = self._db.session.execute(sql, {"user_id":user_id}).fetchall()

        citations = []
        prev_cite_id = -1

        for cite_id, cite_as, entry_type, field_type, field_value in result:
            if prev_cite_id != cite_id:
                citations.append({"cite_id":cite_id, "cite_as":cite_as, "entry_type":entry_type})
                prev_cite_id = cite_id
            citations[-1][field_type] = field_value

        return citations

default_citation_repository = CitationRepository()
