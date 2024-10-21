# -------------------inheritance concept

class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")

class male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name

    def flirt(self):
        print("i can flirt")

    def work(self):
        super().work()
        print("i can code")

male_1=male("piyush",1)
male_1.flirt()
male_1.work()

print(male_1.num_eyes)
print(male_1.name)