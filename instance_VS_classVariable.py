# ------------------------------instance variable vs class variable

# example of instance variable

class employees:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02

    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raised amount is {self.raise_amount}")

emp1=employees("piyush")
emp1.raise_amount=0.3  
emp1.showDetails()

emp2=employees("harry")
emp2.showDetails()

# but you need a variable is permanent for any object creation
# here comes class variable 

class employees:
    companyName="apple"
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02

    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raised amount in {self.companyName} is {self.raise_amount}")

emp1=employees("piyush")
emp1.raise_amount=0.3  
emp1.showDetails()

emp2=employees("harry")
emp2.showDetails()