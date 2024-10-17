# ------------------------------class method as an alternative constructor in python

class employees:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls,str):
        return cls(str.split("-")[0] , str.split("-")[1])

emp1=employees("piyush", 12000)
print(emp1.name)
print(emp1.salary)

str="gopal-230000"
emp2=employees.fromStr(str)
print(emp2.name)
print(emp2.salary)