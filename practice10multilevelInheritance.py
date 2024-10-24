# ----------------------multilevel inheritance level-2

class human:
    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")

class male(human):
    def sleep(self):
        print("i can sleep whle day")

class boy(male):
    def work(self):
        # human.work(self)
        super().work()
        print("i can code")

boy_1=boy()
boy_1.eat()
boy_1.work()