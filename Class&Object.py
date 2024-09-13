# -------------------------class and object in python
class person:
    name="piyush"
    occupation="software developer"
    networth="50k"
    
    def info(self):
        print(f"{self.name} is a {self.occupation} and his salary is {self.networth}")

a=person()
b=person()

a.name="harry"
a.occupation="HR"
a.networth="100k"

b.name="nikita"
b.occupation="tranni"
b.networth="60k"

a.info()
b.info()