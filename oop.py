class Person:
    def __init__(self, name="Usman", country="Nigeria"):
        self.name = name
        self.coutry = country

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        self.__name = val

