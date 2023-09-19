class Person:
    def __init__ (self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
    @classmethod
    def from_string(cls, string):
        name, age, school = string.split("_")
        return cls(name, age, school)



a = Person.from_string("Usman_Akinyemi_Plaksha")
print(f"I am {a.name} {a.age} from {a.school}")
