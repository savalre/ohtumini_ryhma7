class CitationTemplate():
    def __init__(self):
        self._data = {}
    def add_field(self, key, value):
        self._data[key] = value
    def get_data_dict(self):
        return self._data
    def get_data_entry(self, key):
        return self._data[key]

class BookCitation(CitationTemplate):
    def __init__(self):
        CitationTemplate.__init__(self)
        self.required_fields = ['author', 'editor', 'title', 'publisher', 'year']
        self.optional_fields = ['volume','series','address','edition','month','note','key','url']
    def add_required_fields(self, datalist):
        for count, value in enumerate(datalist):
            self.add_field(self.required_fields[count], value)
    def check_required_fields(self):
        for field in self.required_fields:
            if field not in self._data:
                return False
        return True
    def get_required_field_types(self):
        return self.required_fields
    def get_optional_field_types(self):
        return self.optional_fields
    def get_all_field_types(self):
        return self.required_fields + self.optional_fields
        