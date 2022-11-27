class Citation:
    def __init___(self, cite_as, entryname, fieldtypes):
        """Class for saving the cite_as, entry name and field data,values list

        Args:
            cite_as (string): Unique tag for the citation, for citing in text
            entryname (string): Name of the entry
            fieldtypes (List): List of field type and value pairs in tuples
        """
        self.cite_as = cite_as
        self.entryname = entryname
        self.fieldtypes = fieldtypes