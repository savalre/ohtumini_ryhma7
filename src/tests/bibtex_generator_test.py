import unittest
from entities.citation import Citation
from bibtex_generator.bibtex_generator import BibtexGenerator

class TestBibtexGenerator(unittest.TestCase):
    def setUp(self):
        lista = []
        lista.append(("title", "Pythoinin Alkeet"))
        lista.append(("author", "Pekka Python"))
        lista.append(("year", "2002"))
        lista.append(("publisher", "Kaarme Talo"))

        newcitation = Citation("PP", "book", lista)
        self.generator = BibtexGenerator([newcitation])

    def test_generates_correct_string_from_setup_case(self):
        generated_string = self.generator.generate_string()
        expected_result = "@book{PP,\
    author = {Pekka Python},\
    publisher = {Kaarme Talo},\
    title = {Pythoinin Alkeet},\
    year = {2002}\
}"