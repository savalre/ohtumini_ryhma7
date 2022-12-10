"""
Citation
"""
class Citation: # pylint: disable=too-few-public-methods
    """
    Class for saving the cite_as, entry name and field data,values list
    """
    def __init__(self, cite_as, entryname, fieldtypes):
        self.cite_as = cite_as
        self.entryname = entryname
        self.fieldtypes = fieldtypes
