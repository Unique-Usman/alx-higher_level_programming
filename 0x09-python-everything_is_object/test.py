class P:
    def __init__(self, name):
        self.rec = name

    @property
    def rec(self):
        return self.__rec
    @rec.setter
    def rec(self, val):
        self.__rec = val

n = P("Usman")
n.rec = "Arib"
print(n.__dict__)
