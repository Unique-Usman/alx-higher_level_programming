class Coral:
    def community(self):
        print("corals live in a communtity")
    def print_helo(self):
        print("Helo")

class Anemone:
    def protect_clownfish(self):
        print("They protect clownfish")
    def print_helo(self):
        print("Hlo")

class Corealreaf(Coral, Anemone):
    def age(self):
        print("very old")

new = Corealreaf()

new.protect_clownfish()
new.community()
new.print_helo()
