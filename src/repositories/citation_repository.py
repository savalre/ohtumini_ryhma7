"""
CitationRepository
Handles the storing and fetching of citations in the DB
Accepts and returns Citation objects
"""
from sqlalchemy.exc import IntegrityError
from db.db import db
from citation_class.citation_template import BookCitation

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
            citation of type CitationTemplate (or derived from it)
        Returns:
            True if succesful, otherwise False
        """
        data = citation.get_data_dict()

        if "cite_as" not in data:
            return False
        cite_as = data["cite_as"]

        if "entry_type" not in citation:
            return False
        entry_type = citation.get_data_entry("entry_type")

        self._db.session.begin()
        try:
            sql_citation = "INSERT INTO citations (user_id, deleted) \
                    VALUES (:user_id, 0) RETURNING id"
            citation_id = self._db.session.execute(sql_citation, {"user_id": user_id}).fetchone()[0]

            sql_entry_type = "INSERT INTO entry_types (citation_id, type, cite_as) \
                    VALUES (:citation_id, :entry_type, :cite_as)"
            self._db.session.execute(sql_entry_type, {"citation_id": citation_id,
                                                      "entry_type":entry_type, "cite_as":cite_as})

            sql_field = "INSERT INTO fields (citation_id, type, value)\
                    VALUES (:citation_id, :type, :value)"

            for field_type, value in data.items():
                if field_type == "cite_as" or field_type == "entry_type":
                    continue
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
                if prev_cite_id > 0:
                    if not citations[-1].check_required_fields():
                        citations = citations[:-1]
                if entry_type == "book":
                    new_citation = BookCitation()
                citations.append(new_citation)
                prev_cite_id = cite_id
            citations[-1].add_field(field_type, field_value)

        return citations

default_citation_repository = CitationRepository()
