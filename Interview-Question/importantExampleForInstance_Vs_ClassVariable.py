# important example

class employees:
    companyName="apple U.S"
    def __init__(self ,name):
        self.name=name
        self.raised_amount=0.02

    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raised amount in {self.companyName} is {self.raised_amount}")
    
emp1=employees("piyush")
emp1.companyName="apple India"
emp1.showDetails()

# --------------------------------------------------must read---------------------------------------

# ----------------here we did'nt change the value of the class variable companyName
# print(employees.companyName)
# ----------------but in object emp1 we created instance variable with same name and when pyhton gets class and instance variable with same name then python will perfer instance variable first
# print(emp1.companyName)

emp2=employees("harry")
emp2.raised_amount=0.3
emp2.showDetails()