# differntating the age of two person by overloading greater then operator

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        if(self.age>other.age):
            return True
        else:
            return False

p1=person("piyush", 22)
p2=person("pappu", 23)

if(p1>p2):
    print(f"{p1.name} has to pay the bill")
else:
    print(f"{p2.name} has to pay the bill")