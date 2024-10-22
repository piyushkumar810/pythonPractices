# ------------------------single level inheritance

class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("this sound made by an animal")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed

    def make_sound(self):
        print("Bark")

d=dog("dog", "dobberman")
d.make_sound()

a=animal("dog", "dog")
a.make_sound()