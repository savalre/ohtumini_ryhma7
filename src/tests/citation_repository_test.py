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
            self.assertEqual(cite_repo.list_citations(), [])

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

    def test_two_with_same_cite_as_fail(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)
            self.assertRaises(ValueError, cite_repo.store_citation, citation)
    
    def test_delete_one_citation(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)

            citation = Citation("test_cite_as2", "book2", [("author","test_author2")])
            cite_repo.store_citation(citation)

            cite_repo.delete_selected_citations(["test_cite_as2"])

            result = cite_repo.list_citations()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].cite_as, "test_cite_as")

    
    def test_delete_multiple_citations(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)

            citation = Citation("test_cite_as2", "book2", [("author","test_author2")])
            cite_repo.store_citation(citation)

            citation = Citation("test_cite_as3", "book3", [("author","test_author3")])
            cite_repo.store_citation(citation)

            cite_repo.delete_selected_citations(["test_cite_as","test_cite_as3"])

            result = cite_repo.list_citations()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].cite_as, "test_cite_as2")

    
    def test_deleted_citation_not_found_in_list(self):
        with app.app_context():
            citation = Citation("test_cite_as", "book", [("author","test_author")])
            cite_repo.store_citation(citation)

            citation = Citation("test_cite_as2", "book2", [("author","test_author2")])
            cite_repo.store_citation(citation)

            citation = Citation("test_cite_as3", "book3", [("author","test_author3")])
            cite_repo.store_citation(citation)

            cite_repo.delete_selected_citations(["test_cite_as"])

            result = cite_repo.list_citations()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].cite_as, "test_cite_as2")
            self.assertEqual(result[1].cite_as, "test_cite_as3")

    


