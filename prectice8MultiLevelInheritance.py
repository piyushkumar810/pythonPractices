class employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"the name is {self.name}")

class dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"the dance is {self.dance}")

class danceremployee(employee,dancer):
    def __init__(self,dance,name):
        
        self.dance=dance
        self.name=name

cls=danceremployee("kathak", "shivani")
print(cls.name)
print(cls.dance)

cls.show()