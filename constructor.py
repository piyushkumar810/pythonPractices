# ----------------------------constructor in python
class employees:
    def __init__(self,n,o):
        print("piyush kumar is the employee of the year")
        self.name=n
        self.occuation=o
    
    def info(self):
        print(f"{self.name} is a {self.occuation}")

a=employees("piyush", "software developer")
b=employees("divya", "Hr")

a.info()
b.info()