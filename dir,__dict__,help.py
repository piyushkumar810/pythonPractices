# --------------------dir(), __dict__(), and help() method in pyhton

# object introspection --> it means you want to know, what-what things present inside an object and 
#                           how can we use it.
# here these three methods are commanly used to get information about the object


# ---------------------------------------------------------dir() method
x=[1,2,4]
print(x)
print(dir(x))

# -----------output
# [1,2,4]
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
#  '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
# '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
# 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print("\n")


# ------------------------------------------------------ __dict__() attribute
class student:
    def __init__(self, name):
        self.name=name
        self.course="BCA"

    def showDetails(self):
        print(f"the name of the student is {self.name} and the course he applied for {self.course}")

    @staticmethod
    def add(n):
        return (n+n)

std1=student("piyush")
std1.showDetails()

print(std1.add(6))

# lets look all the details of student class
print(std1.__dict__)
print(student.__dict__)
print(dir(student))


# ----------output
# the name of the student is piyush and the course he applied for BCA
# 12
# {'name': 'piyush', 'course': 'BCA'}
# {'__module__': '__main__', '__init__': <function student.__init__ at 0x00000234A2C48AE0>, 'showDetails': <futtion student.showDetails at 0x00000234A2C49940>, 'add': <staticmethod(<function student.add at 0x00000234A2C499E0>)>, '__dict__': <attribute '__dict__' of 'student' objects>, '__weakref__': <attribute '__weakref__' of 'student' objects>, '__doc__': None}
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'showDetails']


# -------------------------------------------------------------help() method
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        self.version=1

p=person("piyush", 22)
print(help(person))