class CitationTemplate():
    """A citation template is a template that is used to create a citation."""
    def __init__(self):
        """_data is a dictionary for storing all of the field and data pairs."""
        self._data = {}
    def add_field(self, key, value):
        """Add a filed and data pair to the data

        Args:
            key (string): The field type
            value (string): field value
        """
        self._data[key] = value
    def get_data_dict(self):
        """return the data dictionary

        Returns:
            dictionary: The data dictionary
        """
        return self._data
    def get_data_entry(self, key):
        """Returns the value for the given field

        Args:
            key (string): The field type

        Returns:
            string: field value
        """
        return self._data[key]

class BookCitation(CitationTemplate):
    def __init__(self):
        """Constructor for the BookCitation class. Initializes the CitationTemplate class
            and sets the required and optional fields for a book citation
        """
        CitationTemplate.__init__(self)
        self.required_fields = ['author', 'editor', 'title', 'publisher', 'year']
        self.optional_fields = ['volume','series','address','edition','month','note','key','url']
    def add_required_fields(self, datalist):
        """Adds the required fields to the citation template in the same
        order as the required_fields list

        Args:
            datalist (list): A list of the required fields values. The order of the list
            must match the order of the required_fields list
        """
        for count, value in enumerate(datalist):
            self.add_field(self.required_fields[count], value)
    def check_required_fields(self):
        """Checks if the citation has all the required fields

        Returns:
            bool: True if all the required fields are present, False otherwise.
        """
        for field in self.required_fields:
            if field not in self._data:
                return False
        return True
    def get_required_field_types(self):
        """Returns the required field types

        Returns:
            list: List of all the required field types
        """
        return self.required_fields
    def get_optional_field_types(self):
        """Returns the optional field types

        Returns:
            list: List of all the optional field types
        """
        return self.optional_fields
    def get_all_field_types(self):
        """Returns all of the possible field types

        Returns:
            list: List of all the possible field types
        """
        return self.required_fields + self.optional_fields
        