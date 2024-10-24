# -------------------------------------hierarchical inheritance in pyhton

class human:
    def __init__(self,name, age):
        print("calling init from human class")
        self.name=name
        self.age=age

    def showDetails(self):
        print(f'the name of student is {self.name} and his age is {self.age}')

    def eat(self):
        print("i can eat")

class male(human):
    def __init__(self, m_name, age, location):
        print("calling init from male class")
        human.__init__(self,m_name,age)
        self.location=location

    def sleep(self):
        print("i can sleep whole day")

class female(human):
    def __init__(self, name, age, can_dance):
        print("calling init from female class")
        super().__init__(name, age)
        self.know_dancing=can_dance

    def showDetails_f(self):
        super().showDetails()
        print(f"know dnacing = {self.know_dancing}")

    def work(self):
        print("i can code")

female_1=female("jaya" , 20, True)
female_1.showDetails_f()
print(female_1.age)