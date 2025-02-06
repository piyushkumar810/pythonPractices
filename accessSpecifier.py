#---------------------------------- Access specifier in python

# ------------public access specifier
class employees:
    def __init__(self):
        self.name="piyush"

a=employees()
print(a.name)
print("\n")

# -----------private access specifier 
class students:
    def __init__(self):
        self.__names="piyush"



b=students()
# print(b.__names)----->cannot accessed directily because it is private variable
print(b._students__names)
# note--> _students__names this syntax is called name mangling (it is a technique used to protect class private and super class private attribute from being accendientally overwritten)
print("\n")

# ------------protected accecc specifier
class chief:
    def __init__(self):
        self._name="piyush"
    
    def _funname(self):
        return "mashla dosha"
    
class waiter(chief):
    pass

obj=chief()
obj1=chief()

print(obj._name)
print(obj1._funname())



# remember
# it is important to note that the single underscore is just a  naming convention and does not provide 
# any protected or restricted access to the member