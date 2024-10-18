# --------------------------accessing parent constructor using super keyword

class employees:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(employees):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

piyush=employees("piyush kumar", 201)
harry=programmer("harry bahi", 205, "python")

print(harry.name)
print(harry.id)
print(harry.lang)