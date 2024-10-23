# -----------------------multi level inheritance

class human:
    can_breath=True
    def __init__(self,num_heart):
        print("calling init from human")
        self.eyes=2
        self.heart=num_heart

    def eat(self):
        print("i want to eat")

    def work(self):
        print("i can work")

class male(human):
    def __init__(self,name):
        print("calling init form male class")
        self.name=name

    def sleep(self):
        print("i can sleep whole day")

class boy(male):
    def __init__(self,heart,name,can_dance):
        human.__init__(self,heart)
        male.__init__(self,name)
        self.know_dance=can_dance

    def work(self):
        # human.work(self)
        super().work()
        print("i can code")

boy_1=boy(1,"rahul", True)
print(boy_1.name)
print(boy_1.know_dance)
print(boy_1.can_breath)

print(boy.mro())