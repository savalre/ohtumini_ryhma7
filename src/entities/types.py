class Types:
    def __init__(self):
        self.values = []

    def article(self):
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
    