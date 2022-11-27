import unittest
from citation_class.citation_template import CitationTemplate, BookCitation

class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.template = CitationTemplate()
    
    def test_add_fields(self):
        self.template.add_field('author', 'Test Author')
        self.assertEqual(self.template._data['author'], 'Test Author')
    
    def test_get_data_dict(self):
        self.template.add_field('author', 'Test Author')
        self.assertEqual(self.template.get_data_dict(), {'author': 'Test Author'})

    def test_get_data_entry(self):
        self.template.add_field('author', 'Test Author')
        self.assertEqual(self.template.get_data_entry('author'), 'Test Author')

class TestBookCitation(unittest.TestCase):
    def setUp(self):
        self.book = BookCitation()
    
    def test_get_required_field_types(self):
        self.assertEqual(self.book.get_required_field_types(), ['author', 'editor', 'title', 'publisher', 'year'])

    def test_get_optional_field_types(self):
        self.assertEqual(self.book.get_optional_field_types(), ['volume', 'series', 'address', 'edition', 'month', 'note', 'key', 'url'])

    def test_get_all_fields(self):
        self.assertEqual(self.book.get_all_field_types(), ['author', 'editor', 'title', 'publisher', 'year', 'volume', 'series', 'address', 'edition', 'month', 'note', 'key', 'url'])

    def test_add_required_fields(self):
        self.book.add_required_fields(['Test Author', 'Test Editor', 'Test Title', 'Test Publisher', 'Test Year'])
        test_dict = {'author': 'Test Author',
        'editor': 'Test Editor',
        'title': 'Test Title',
        'publisher': 'Test Publisher', 
        'year': 'Test Year'}
        
        self.assertEqual(self.book.get_data_dict(), test_dict)

    def test_check_required_fields_after_adding_enough(self):
        self.book.add_required_fields(['Test Author', 'Test Editor', 'Test Title', 'Test Publisher', 'Test Year'])
        self.assertTrue(self.book.check_required_fields())

    def test_check_required_fields_afer_not_adding_anything(self):
        self.assertFalse(self.book.check_required_fields())
    
    def test_check_required_fields_after_adding_too_little(self):
        self.book.add_field('author', 'Test Author')
        self.assertFalse(self.book.check_required_fields())