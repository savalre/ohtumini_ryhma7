"""
CitationByDoi
Fetches the citation data from the ACM web library
by doi
"""
from bs4 import BeautifulSoup

class CitationByDoi:
    """
    Uses the BeautifulSoup library to parse relevant metadata
    from the article's page
    Accepts doi as a string as a parameter
    Returns a dictionary of the metadata or an error message
    """
    def __init__(self, content):
        self._soup = BeautifulSoup(content, 'html.parser')

    def get_references(self):
        """
        Handles the creation of the metadata dictionary

        Returns:
            Dictionary of the metadata
        """
        data = {}
        data['author'] = self.get_authors()
        data['title'] = self.get_title()
        data['booktitle'] = self.get_journal()
        data['type'] = self.get_type(data['booktitle'])
        data['year'] = self.get_year()
        if data['type'] == 'article':
            data['volume'] = self.get_volume()
            data['journal'] = data['booktitle']
            del data['booktitle']
        return data

    def get_authors(self):
        """
        Parses the author names from the html soup
        """
        authors_list = []
        for author in self._soup.find_all(class_="loa__author-name"):
            authors_list.append(author.get_text())
        authors = (" and ").join(authors_list)
        return authors

    def get_title(self):
        """
        Parses the article title from the html soup
        """
        title = self._soup.find(class_="citation__title")
        return title.get_text()

    def get_journal(self):
        """
        Parses the publication name from the html soup
        """
        journal = self._soup.find(class_="epub-section__title")
        return journal.get_text()

    def get_year(self):
        """
        Parses the publication year from the html soup
        """
        raw = self._soup.find(class_="epub-section__date").get_text()
        year = raw.split()[1]
        return year

    def get_type(self,title):
        """
        Determines the type of the citation by the title of
        the publication
        """
        words = title.split()
        if "Proceedings" in words:
            return "inproceedings"
        return "article"

    def get_volume(self):
        """
        Parses the volume of the publication from the html soup
        """
        raw = self._soup.find(class_="comma-separator").get_text()
        volume = raw.split()[1]
        return volume
