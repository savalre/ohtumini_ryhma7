import unittest
from entities.citation import Citation
from bibtex_generator.bibtex_generator import generate_bibtex_string

class TestBibtexGenerator(unittest.TestCase):
    def setUp(self):
        lista = []
        lista.append(("title", "Pythoinin Alkeet"))
        lista.append(("author", "Pekka Python"))
        lista.append(("year", "2002"))
        lista.append(("publisher", "Kaarme Talo"))

        self.newcitation = Citation("PP", "book", lista)
    

    def test_generates_correct_string_from_setup_case(self):
        generated_string = generate_bibtex_string([self.newcitation])
        expected_result = "@book{PP,\n    author = {Pekka Python},\n    publisher = {Kaarme Talo},\n    title = {Pythoinin Alkeet},\n    year = {2002}\n}\n"
        assert expected_result == generated_string