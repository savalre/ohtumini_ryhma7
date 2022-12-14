"""
CitationByDoi
Fetches the citation data from the ACM web library
by doi
"""
class CitationByDoi:
    """
    Uses the BeautifulSoup library to parse relevant metadata
    from the article's page
    Accepts doi as a string as a parameter
    Returns a dictionary of the metadata or an error message
    """
    def __init__(self, content):
        self.content = content
        self.type = self.get_type(self.content['type'])

    def get_references(self):
        """
        Calls the correct function to build the metadata dictionary

        Returns:
            Dictionary of the metadata
        """
        if self.type == "book":
            data = self.get_book_data()
        if self.type == "inproceedings":
            data = self.get_inproceedings_data()
        if self.type == "article":
            data = self.get_article_data()
        if self.type == "phdthesis":
            data = self.get_phdthesis_data()
        if self.type == "techreport":
            data = self.get_techreport_data()
        if self.type == "proceedings":
            data = self.get_proceedings_data()
        if self.type == "inbook":
            data = self.get_inbook_data()
        return data

    def get_book_data(self):
        """
        Creates dict for book types
        """
        citation = {"type":"book"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["year"] = self.get_year()
        citation["publisher"] = self.content["publisher"]
        return citation

    def get_inproceedings_data(self):
        """
        Creates dict for inproceedings types
        """
        citation = {"type":"inproceedings"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["booktitle"] = self.content["container-title"]
        citation["year"] = self.get_year()
        return citation

    def get_article_data(self):
        """
        Creates dict for article types
        """
        citation = {"type":"article"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["journal"] = self.content["container-title"]
        citation["year"] = self.get_year()
        if self.content.get("volume") is None:
            citation["volume"] = self.content["issue"]
        else:
            citation["volume"] = self.content["volume"]
        return citation

    def get_phdthesis_data(self):
        """
        Creates dict for phdthesis types
        """
        citation = {"type":"phdthesis"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["school"] = self.content["publisher"]
        citation["year"] = self.get_year()
        return citation

    def get_techreport_data(self):
        """
        Creates dict for techreport types
        """
        citation = {"type":"techreport"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["institution"] = self.content["publisher"]
        return citation

    def get_proceedings_data(self):
        """
        Creates dict for proceedings types
        """
        citation = {"type":"proceedings"}
        citation["title"] = self.content["title"]
        citation["year"] = self.get_year()
        return citation

    def get_inbook_data(self):
        """
        Creates dict for inbook types
        """
        citation = {"type":"inbook"}
        citation["author"] = self.get_authors()
        citation["title"] = self.content["title"]
        citation["pages"] = self.content["page"]
        citation["publisher"] = self.content["publisher"]
        citation["year"] = self.get_year()
        return citation

    def get_authors(self):
        """
        Gets the author(s) from the dictionary
        """
        authors = []
        authors_raw = self.content["author"]
        for author in authors_raw:
            authors.append(f"{author['given']} {author['family']}")
        return " and ".join(authors)

    def get_year(self):
        """
        Gets the year from the dictionary
        """
        return self.content["issued"]["date-parts"][0][0]

    def get_type(self,raw_type):
        """
        Determines the type of the publication by the type in the
        dictionary
        """
        entry_type = ""
        type_dict = {"article":["ARTICLE","ARTICLE_JOURNAL","ARTICLE_MAGAZINE",
                                "ARTICLE_NEWSPAPER"],
                     "book":["BOOK"],
                     "inproceedings":["PAPER_CONFERENCE"],
                     "phdthesis":["THESIS"],
                     "techreport":["REPORT"],
                     "inbook":["CHAPTER"]
                     }
        for key, values in type_dict.items():
            if raw_type in values:
                entry_type = key
        if self.content.get("genre") == "proceeding" and entry_type == "book":
            entry_type = "proceedings"
        return entry_type
