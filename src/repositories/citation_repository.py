from db.db import db

class PlaceholderCitation:
    def __init__(self, entry_type, data):
        self.entry_type = entry_type
        self.data = data

class CitationRepository:
    def __init__(self, db=db):
        self._db = db

    def store_citation(self, citation):
        #PLACEHOLDER CODE TO GET USER_ID FROM SESSION
        user_id = 1
        #PLACEHOLDER CODE TO EXTRACT DATA FROM CITATION CLASS
        entry_type = citation.entry_type
        cite_as = "test"
        data = citation.data

        self._db.session.begin()
        try:
            sql_citation = "INSERT INTO citations (user_id, deleted) VALUES (:user_id, 0) RETURNING id"
            citation_id = self._db.session.execute(sql_citation, {"user_id": user_id}).fetchone()[0]

            sql_entry_type = "INSERT INTO entry_types (citation_id, type, cite_as, deleted)}
                    VALUES (:citation_id, :entry_type, :cite_as, 0)"
            self._db.session.execute(sql_entry_type,
                                     {"citation_id": citation_id, "entry_type":entry_type, "cite_as":cite_as})

            sql_field = "INSERT INTO fields (citation_id, type, value, deleted)\
                    VALUES (:citation_id, :type, :value, 0)"

            for field_type, value in data:
                self._db.session.execute(sql_field, {"citation_id": citation_id, "type":field_type, "value" :value})
            self._db.session.commit()
            return True
        except Exception as e:
            print(e)
            self._db.session.rollback()
            return False

default_citation_repository = CitationRepository()
