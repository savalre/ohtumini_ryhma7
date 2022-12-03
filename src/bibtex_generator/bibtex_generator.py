"""
Function for generating a BibTex string
Uses the bibtexparser library to encode the citations
"""

from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def generate_bibtex_string(citation_list):
    """
        The function recieves a list of Citation objects
        which are converted into the BibTex format.
        The function formats the given list into
        the format used by the bibtexparser library.

    Args:
        citation_list (List): List of Citation objects
    """
    bib_database = BibDatabase()

    for i, citation in enumerate(citation_list):
        bib_database.entries.append({})
        current_dictionary = bib_database.entries[i]

        current_dictionary["ENTRYTYPE"] = citation.entryname
        current_dictionary["ID"] = citation.cite_as

        for field in citation.fieldtypes:
            current_dictionary[field[0]] = field[1]

    writer = BibTexWriter()
    writer.indent = '    '
    return writer.write(bib_database)
