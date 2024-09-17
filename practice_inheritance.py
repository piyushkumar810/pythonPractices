class employees:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"the name of employees is {self.name} and his id is {self.id} ")

class programm(employees):
    def showlanguage(self):
        print("the default language is pyhton")

e1=employees("piyush", 101)
e1.showDetails()
e2=programm("rohaini", 105)
e2.showDetails()
e2.showlanguage()