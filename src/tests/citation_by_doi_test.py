import os
import unittest
from bs4 import BeautifulSoup
from doi.citation_by_doi import CitationByDoi

dirname = os.path.dirname(__file__)
path1 = os.path.join(dirname, "dummy_page.html")
path2 = os.path.join(dirname, "dummy_page_article.html")

class TestCitationByDoi(unittest.TestCase):
    def setUp(self):
        with open(path1) as page1:
            content1 = page1.read()

        self.doi1 = CitationByDoi(content1)

        with open(path2) as page2:
            content2 = page2.read()

        self.doi2 = CitationByDoi(content2)

    def test_correct_multiple_authors(self):
        authors = self.doi1.get_authors()
        self.assertEqual(authors, "Moti Motivaatio and Maija Masis" )

    def test_correct_title(self):
        title = self.doi1.get_title()
        self.assertEqual(title, "Motivaation Puute")

    def test_correct_journal_name(self):
        journal = self.doi1.get_journal()
        self.assertEqual(journal, "14th Annual LOM Meeting Proceedings")

    def test_correct_publication_type(self):
        journal = self.doi1.get_journal()
        entry_type = self.doi1.get_type(journal)
        self.assertEqual(entry_type, "inproceedings")

    def test_correct_publication_year(self):
        year = self.doi1.get_year()
        self.assertEqual(year, "2022")

    def test_correct_output_length(self):
        data = self.doi1.get_references()
        self.assertEqual(len(data), 5)

    def test_correct_key_inproceedings(self):
        data = self.doi1.get_references()
        self.assertEqual(data['booktitle'], "14th Annual LOM Meeting Proceedings")

    def test_correct_single_author(self):
        author = self.doi2.get_authors()
        self.assertEqual(author, "Moti Motivaatio")

    def test_correct_publication_type_article(self):
        journal = self.doi2.get_journal()
        entry_type = self.doi2.get_type(journal)
        self.assertEqual(entry_type, "article")

    def test_correct_volume(self):
        volume = self.doi2.get_volume()
        self.assertEqual(volume, "233")

    def test_correct_output_length_article(self):
        data = self.doi2.get_references()
        self.assertEqual(len(data), 6)

    def test_correct_key_article(self):
        data = self.doi2.get_references()
        self.assertEqual(data['journal'], "Motivaatio ja sen puute")
