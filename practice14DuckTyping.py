class Duck:
    def swim(self):
        print("i am a duck and i can swim")

    def speak(self):
        print("quack quack ")

class Dog:
    def swim(self):
        print("i am dog and i can swim")

    def speak(self):
        print("woof woof ")

class person:
    def speak(self):
        print("i am a person")

def display(obj):
    obj.swim()
    obj.speak()
    print("information displayed")

d=Duck()
dog=Dog()
p=person()

display(d)
# display(p)----------- this will give error because person class doesn't have swim method