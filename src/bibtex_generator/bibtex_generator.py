from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

class BibtexGenerator():
    """
    Class for generating a BibTex string
    Uses the bibtexparser library to encode the citations
    The constructor recieves a list of Citation objects
    which are converted into the BibTex format
    """
    def __init__(self, citation_list):
        self.db = BibDatabase()

        for i in range(len(citation_list)):
            current_citation = citation_list[i]
            self.db.entries.append({})
            current_dictionary = self.db.entries[i]

            current_dictionary["ENTRYTYPE"] = current_citation.entryname
            current_dictionary["ID"] = current_citation.cite_as

            for field in current_citation.fieldtypes:
                current_dictionary[field[0]] = field[1]

    def generate_string(self):
        """
        This method generates and returns the citations in
        a BibTex format as a string using the BibTexWriter 
        class from the bibtexparser library.
        """
        writer = BibTexWriter()
        writer.indent = '    '
        return(writer.write(self.db))
