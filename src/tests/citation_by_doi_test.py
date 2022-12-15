import os
import json
import unittest
from doi.citation_by_doi import CitationByDoi

dirname = os.path.dirname(__file__)
article_path = os.path.join(dirname, "dummyarticle.json")
book_path = os.path.join(dirname, "dummybook.json")
inbook_path = os.path.join(dirname, "dummyinbook.json")
phdthesis_path = os.path.join(dirname, "dummythesis.json")
inproceedings_path = os.path.join(dirname, "dummyinproceedings.json")
proceedings_path = os.path.join(dirname, "dummyproceedings.json")
techreport_path = os.path.join(dirname, "dummytechreport.json")
article2_path = os.path.join(dirname, "dummyarticle2.json")

class TestCitationByDoi(unittest.TestCase):
    def setUp(self):
        with open(article_path) as data1:
            content1 = json.load(data1)

        self.article = CitationByDoi(content1)

        with open(book_path) as data2:
            content2 = json.load(data2)

        self.book = CitationByDoi(content2)

    def test_correct_multiple_authors(self):
        authors = self.book.get_authors()
        self.assertEqual(authors, "Moti Motivaatio and Maija Masis" )

    def test_correct_single_author(self):
        author = self.article.get_authors()
        self.assertEqual(author, "Moti Motivaatio")

    def test_correct_publication_year(self):
        year = self.article.get_year()
        self.assertEqual(year, 2022)

    def test_correct_output_length_book(self):
        data = self.book.get_references()
        self.assertEqual(len(data), 5)

    def test_correct_output_length_article(self):
        data = self.article.get_references()
        self.assertEqual(len(data), 6)

    def test_correct_output_length_inproceedings(self):
        with open(inproceedings_path) as file:
            content = json.load(file)

        inproceedings = CitationByDoi(content)
        data = inproceedings.get_references()
        self.assertEqual(len(data), 5)

    def test_correct_output_length_proceedings(self):
        with open(proceedings_path) as file:
            content = json.load(file)

        proceedings = CitationByDoi(content)
        data = proceedings.get_references()
        self.assertEqual(len(data), 3)

    def test_correct_output_length_inbook(self):
        with open(inbook_path) as file:
            content = json.load(file)

        inbook = CitationByDoi(content)
        data = inbook.get_references()
        self.assertEqual(len(data), 6)

    def test_correct_output_length_techreport(self):
        with open(techreport_path) as file:
            content = json.load(file)

        techreport = CitationByDoi(content)
        data = techreport.get_references()
        self.assertEqual(len(data), 4)

    def test_correct_output_length_phdthesis(self):
        with open(phdthesis_path) as file:
            content = json.load(file)

        phdthesis = CitationByDoi(content)
        data = phdthesis.get_references()
        self.assertEqual(len(data), 5)

    def test_article_with_no_volume_length(self):
        with open(article2_path) as file:
            content = json.load(file)

        article = CitationByDoi(content)
        data = article.get_references()
        self.assertEqual(len(data), 6)
