# ----------------------multilevel inheritance level-3

class human:
    def __init__(self,num_heart):
        print("calling init method from human class ")
        self.eyes=2
        self.heart=num_heart

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

boy_1=boy(1)
boy_1.eat()
boy_1.work()
print(boy_1.heart)
print(boy_1.eyes)

print(boy.mro())