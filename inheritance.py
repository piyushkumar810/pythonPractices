# ----------------------------inheritance in python

class base:
    def display(self):
        print("hello base class")

class child(base):
    def display2(self):
        print("hello child class")

x=child()
x.display()
x.display2()