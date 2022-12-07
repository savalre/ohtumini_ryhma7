"""
Type
"""
class Types:
    """
    Class for generating different field types based on the entry type
    """
    def __init__(self):
        self.values = []
        self.entry_types = [
            "article",
            "book",
            "booklet",
            "conference",
            "inbook",
            "incollection",
            "inproceedings",
            "manual",
            "mastersthesis",
            "misc",
            "phdthesis",
            "proceedings",
            "techreport",
            "unpublished",
        ]

    def article(self):
        """Method for generating field types of the entry type article"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("journal", True),
            ("year", True),
            ("volume", True),

            ("number", False),
            ("pages", False),
            ("month", False),
            ("doi", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def book(self):
        """Method for generating field types of the entry type book"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("publisher", True),
            ("year", True),

            ("volume", False),
            ("series", False),
            ("address", False),
            ("edition", False),
            ("month", False),
            ("note", False),
            ("key", False),
            ("url", False)
        ]
        return self.values

    def booklet(self):
        """Method for generating field types of the entry type booklet"""
        self.values = [
            ("cite_as", True),
            ("title", True),

            ("author", False),
            ("howpublished", False),
            ("address", False),
            ("month", False),
            ("year", False),
            ("edition", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def conference(self):
        """Method for generating field types of the entry type conference"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("booktitle", True),
            ("year", True),

            ("editor", False),
            ("volume", False),
            ("series", False),
            ("pages", False),
            ("address", False),
            ("month", False),
            ("organization", False),
            ("publisher", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def inproceedings(self):
        """Method for generating field types of the entry type inproceedings"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("booktitle", True),
            ("year", True),

            ("editor", False),
            ("volume", False),
            ("series", False),
            ("pages", False),
            ("address", False),
            ("month", False),
            ("organization", False),
            ("publisher", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def inbook(self):
        """Method for generating field types of the entry type inbook"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("pages", True),
            ("publisher", True),
            ("year", True),

            ("volume", False),
            ("series", False),
            ("type", False),
            ("address", False),
            ("edition", False),
            ("month", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def incollection(self):
        """Method for generating field types of the entry type incollection"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("booktitle", True),
            ("publisher", True),
            ("year", True),

            ("editor", False),
            ("volume", False),
            ("series", False),
            ("type", False),
            ("chapter", False),
            ("pages", False),
            ("address", False),
            ("edition", False),
            ("month", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def manual(self):
        """Method for generating field types of the entry type manual"""
        self.values = [
            ("cite_as", True),
            ("title", True),

            ("author", False),
            ("organization", False),
            ("address", False),
            ("edition", False),
            ("month", False),
            ("year", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def mastersthesis(self):
        """Method for generating field types of the entry type mastersthesis"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("school", True),
            ("year", True),

            ("type", False),
            ("address", False),
            ("month", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def misc(self):
        """Method for generating field types of the entry type misc"""
        self.values = [
            ("cite_as", True),

            ("author", False),
            ("title", False),
            ("howpublished", False),
            ("month", False),
            ("year", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def phdthesis(self):
        """Method for generating field types of the entry type phdthesis"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("school", True),
            ("year", True),

            ("type", False),
            ("address", False),
            ("month", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def proceedings(self):
        """Method for generating field types of the entry type proceedings"""
        self.values = [
            ("cite_as", True),
            ("title", True),
            ("year", True),

            ("editor", False),
            ("volume", False),
            ("series", False),
            ("address", False),
            ("month", False),
            ("publisher", False),
            ("organization", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def techreport(self):
        """Method for generating field types of the entry type techreport"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("institution", True),
            ("year", True),

            ("type", False),
            ("number", False),
            ("address", False),
            ("month", False),
            ("note", False),
            ("key", False)
        ]
        return self.values

    def unpublished(self):
        """Method for generating field types of the entry type unpublished"""
        self.values = [
            ("cite_as", True),
            ("author", True),
            ("title", True),
            ("note", True),

            ("month", False),
            ("year", False),
            ("key", False)
        ]
        return self.values
    