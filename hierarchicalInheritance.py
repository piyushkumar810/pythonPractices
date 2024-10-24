# ---------------------------------hierarchical inheritance in python

class human:
    def eat(self):
        print("i can eat")

class male(human):
    def sleep(self):
        print("i can sleep whole day")

class female(human):
    def work(self):
        print("i can code")

fem_1=female()
fem_1.eat()

mal_1=male()
mal_1.eat()