class My_defaultdict(dict):
    ## ????
    def __init__(self, default_factory = None):
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.defaultFactory is None:
            raise KeyError(key)
        self[key] = My_defaultdict(self.defaultFactory)
        return self[key]

    def __getitem__(self, key):
        if key not in self.iterkeys():
            My_defaultdict.__missing__(self, key)
        return super(My_defaultdict, self).__getitem__(key)


