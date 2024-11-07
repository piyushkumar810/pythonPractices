# ----------------------------------------method overloading in python

# in python there is no concept called method overloading because pyhton does not support method overloading

# what is method overloading ?
# ans --> when multiple method whith the same name but with different no of argument within the same class
#          is called method overloading


# though python doesn't support method overloading but we can overolade method

# there are two way to overloade method

# 1st ----------------- by default argument
# eg


class Demo:
    def add(self, a, b, c=0):
        return a+b+c
    
d=Demo()
print(d.add(2,5))
print(d.add(1,4,7))
print("\n")


# 2nd----------------- by passing *args

class Demo1:
    def add1(self, *args):
        temp=0
        for i in args:
            temp=temp+i
        return temp
    
d1=Demo1()
print(d1.add1(2,4))
print(d1.add1(2,4,6))
print(d1.add1(2,4,8,23))
print(d1.add1(34,5,7,6,23,56,67,32))