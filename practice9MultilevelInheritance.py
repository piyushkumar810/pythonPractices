# ----------------------multilevel inheritance level-1

class human:
    def eat(self):
        print("i can eat")

class male(human):
    def sleep(self):
        print("i can sleep whle day")

class boy(male):
    pass

boy_1=boy()
boy_1.eat()