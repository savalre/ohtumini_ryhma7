"""
Citation
"""
class Citation:
    """
    Class for saving the cite_as, entry name and field data,values list
    """
    def __init__(self, cite_as, entryname, fieldtypes):
        self.cite_as = cite_as
        self.entryname = entryname
        self.fieldtypes = fieldtypes

    def true(self):
        """Useless method for pylint tests"""
        return True

    def false(self):
        """Useless method for pylint tests"""
        return False
