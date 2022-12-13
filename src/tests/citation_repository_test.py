import unittest
from entities.citation import Citation
from app import app
from db.init_db import init_db
import repositories.citation_repository
init_db()
cite_repo = repositories.citation_repository.default_citation_repository

class TestCitationRepository(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            cite_repo.clear_citations()

    def test_list_empty_after_clear(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)
            cite_repo.clear_citations()
            self.assertEqual(len(cite_repo.list_citations()), 0)

    def test_list_with_one_citations(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)
            result = cite_repo.list_citations()[0]
            self.assertEqual(result.cite_as, "test_cite_as")
            self.assertEqual(result.entryname, "book")
            self.assertTrue(("author", "test_author") in result.fieldtypes)

    def test_list_two_citations_with_same_user(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)
            
            citation = Citation("test_cite_as2", "book2", [("author","test_author2")])
            cite_repo.store_citation(citation)
            
            result = cite_repo.list_citations()[0]
            self.assertEqual(result.cite_as, "test_cite_as")
            self.assertEqual(result.entryname, "book")
            self.assertTrue(("author", "test_author") in result.fieldtypes)
    
            result = cite_repo.list_citations()[1]    
            self.assertEqual(result.cite_as, "test_cite_as2")
            self.assertEqual(result.entryname, "book2")
            self.assertTrue(("author", "test_author2") in result.fieldtypes)

    def test_list_filter(self):
        with app.app_context():
            citation = Citation("BK34", "VOO", [("year",2022)])
            cite_repo.store_citation(citation)

            result = cite_repo.list_citations("2022")[0]
            self.assertEqual(result.cite_as, "BK34")