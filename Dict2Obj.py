class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """
    def __init__(self, dictionary):
        """TODO: Docstring for __init__.

        :dictionary: Input dictionary to be converted
        :returns: Object with attrs as dictionary keys

        """
        for key in dictionary:
            setattr(self, key, dictionary[key])

        self._dict = dictionary.copy()
        pass
