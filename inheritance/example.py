class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelisd="False"):
        self.skeleton = skeleton
        self.eyelisd = eyelisd
        self.first_name = first_name
        self.last_name = last_name
    def swim(self):
        print("This Fish is swimming")

    def swim_b(self):
        print("The fish swim back")

class Trout(Fish):
    def __init__(self):
        super().__init__(self)

Tri = Trout()
Tri.first_name = "Terry"
print(Tri.first_name )
#jacob = Trout("Jacob")

#print(jacob.first_name)

class Clownfish(Fish):
    def live(self):
        print("The clownfish lives with me")

#casey = Clownfish("cassey")
#print(casey.first_name + " " + casey.last_name)
#casey.swim()

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="catilage", eyelisd=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelisd = eyelisd
    def swim_b(self):
            print("The shark cannot swim backward")

bull = Shark("mute")
print(bull.swim_b())
bull.swim()
