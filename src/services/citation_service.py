"""
Module for validating citations
"""
import re

class UserInputError(Exception):
    """
    UserInputError
    """


class CitationService():
    """
    Class for validating citations
    """

    def __init__(self):
        self.cite_as = ""
        self.fieldtypes = ""

    def validate(self, citation):
        """
        Function checks citations on fields that are prone to errors
        """
        cite_as = citation.cite_as
        fields = citation.fieldtypes

        checked = ["month","year","doi","chapter","volume","pages"]

        if len(cite_as) < 2:
            raise UserInputError("Cite should be over two characters long")

        for field in fields:
            if field[0] == "month" and (not re.match('[0-1][0-9]{1}',
                str(field[1])) or int(field[1]) > 12):

                raise UserInputError("Month should be a valid month in form of: ##")

            if field[0] == "year" and (not re.match('[1-3][0-9]{3}', str(field[1]))):
                raise UserInputError("Not a valid year")

            if field[0] == "doi" and (not re.match('^10[.][0-9]{4,}', str(field[1]))):
                raise UserInputError("Not a valid doi")

            if field[0] == "chapter" or field[0] == "volume":
                if not re.match('[0-9]', str(field[1])):
                    raise UserInputError("Chapter and/or volume should be a number(s)")

            if field[0] == "pages" and (not re.match('[0-9,;]', str(field[1]))):
                raise UserInputError("Page numbers should be separated either by ',' or ';' ")

            if field[0] not in checked and len(str(field[1])) < 2:
                raise UserInputError("Text fields should contain atleast two characters")

        return True

    def filter_to_selected(self, citations, selection_list):
        """
        Function that take a list of citations and 'cite_as' tags.
        Returns a list containing the citation objects whose 'cite_as'
        appears in the selection list.
        """
        selection_set = set(selection_list)
        filtered_list = [cite for cite in citations if cite.cite_as in selection_set]
        return filtered_list

    def convert_list_into_dict(self, citation_list):
        citation_dict = {}
        i = 0
        for citation in citation_list:
            title = ""
            author = ""
            year = ""
            for field_type in citation.fieldtypes:
                if field_type[0] == "title": title = field_type[1]
                elif field_type[0] == "author": author = field_type[1]
                elif field_type[0] == "year": year = field_type[1]

            citation_dict[i] = {
                "entry_type": citation.entryname,
                "cite_as": citation.cite_as, 
                "title": title,
                "author": author,
                "year": year
            }
            i = i + 1
        return citation_dict
