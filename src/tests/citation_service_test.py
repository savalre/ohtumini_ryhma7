import unittest
from entities.citation import Citation
from db.init_db import init_db
from services.citation_service import CitationService, UserInputError

init_db()

class TestCitationService(unittest.TestCase):

    def setUp(self):
        self.cite_serve = CitationService()

    def test_validate_citation_with_too_short_cite_as(self):
        citation = Citation("t", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2022)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Cite should be over two characters long' in str(context.exception))

    def test_validate_citation_with_invalid_year(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",20)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Not a valid year' in str(context.exception))

    def test_validate_citation_with_too_large_year(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",5020)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Not a valid year' in str(context.exception))

    def test_validate_citation_with_invalid_month(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("month",13)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Month should be a valid month in form of: ##' in str(context.exception))
    
    def test_validate_citation_with_malformatted_month(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("month",3)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Month should be a valid month in form of: ##' in str(context.exception))

    def test_validate_citation_with_invalid_doi(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("doi",243211)])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Not a valid doi' in str(context.exception))
    
    def test_validate_citation_with_invalid_chapter(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("volume","voluumi")])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Chapter and/or volume should be a number(s)' in str(context.exception))

    def test_validate_citation_with_invalid_volume(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("chapter","chaptaari")])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Chapter and/or volume should be a number(s)' in str(context.exception))

    def test_validate_citation_with_invalid_pages(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("pages","sivut 2 ja 3")])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Page numbers should be separated either by ',' or '";"' ' in str(context.exception))

    def test_validate_citation_with_too_short_textfield(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),("misc","s")])

        with self.assertRaises(UserInputError) as context:
            self.cite_serve.validate(citation)
            
        self.assertTrue('Text fields should contain atleast two characters' in str(context.exception))
    
    def test_with_all_fields_valid(self):
        citation = Citation("test_cite", "book", [("author","test_author"),("title","test_title"),("publisher","test_publisher"),("year",2020),
                            ("volume","23"), ("series","testi_sarja"), ("address", "Testikatu4"), ("edition", "testi_edition"), ("month", 11), ("note", "testi_note"),
                            ("key", "testi_avain"), ("url", "www.comcom")])

        testValue = self.cite_serve.validate(citation)

        message = "Test value is not true."


        self.assertTrue(testValue, message)

    def test_filter_by_selection(self):
        citations = [
                    Citation("Cite1", None, None),
                    Citation("Cite2", None, None),
                    Citation("Cite3", None, None),
                    Citation("Cite4", None, None),
                    ]

        selection1 = ["Cite1"]
        selection2 = ["Cite2"]
        selection3 = ["Cite1", "Cite4"]
        selection4 = ["Cite1", "Cite2", "Cite3", "Cite4"]
        self.assertEqual(self.cite_serve.filter_to_selected(citations, selection1), citations[0:1])
        self.assertEqual(self.cite_serve.filter_to_selected(citations, selection2), citations[1:2])
        self.assertEqual(self.cite_serve.filter_to_selected(citations, selection3), [citations[0], citations[3]])
        self.assertEqual(self.cite_serve.filter_to_selected(citations, selection4), citations)
