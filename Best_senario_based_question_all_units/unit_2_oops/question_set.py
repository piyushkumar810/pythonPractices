# 🔹 UNIT–2
# OOP & Advanced Concepts (Very Important)
# Section A – OOP Programs
'''
Q1.Create a class BankAccount with:
Class variable to count accounts
Deposit & Withdraw methods
Raise exception if balance < minimum
'''
'''
Q2.Write a Python program to:

Demonstrate method overriding

Use super() explicitly
'''
'''
Q3.Create a class Matrix and overload:

+ for matrix addition

== to compare two matrices
'''
'''
Q4.Write a program using composition:

Car has Engine

Display engine details via car object
'''


# Section B – Inheritance & Polymorphism
'''
Q5.Create a base class Shape
Derived classes: Rectangle, Circle
Override area() method
Store all objects in a list and compute total area
'''
'''
Q6.Write a program to:
Check object type using isinstance
Display different output for different classes
'''


# Section C – Output Based
# Q7
class A:
    x = 10
    def __init__(self):
        self.x = 20

a = A()
print(A.x, a.x)

# Q8
class Test:
    def __init__(self):
        print("Init")

    def __del__(self):
        print("Del")

t = Test()
del t

# ------------------------- question set(pyq)
'''
Q2 (a)
Write an Object-Oriented Program to create a class Complex with img, real and use operator overloading to multiply two complex numbers.
'''

'''
Q2 (b)

Write an OOP program in Python to create a class to read and add two distances.
Use two member functions get_distance and show_distance
Read and display distance in kms and mts
Use a class variable that counts the different values stored
Use add_distance to add distances
'''

'''
Q2 (c)
Write an Object-Oriented program in Python to create a class called person with data members name and age.
Create an inherited class employee with data member department.

Check whether a given person is an employee or not

Display the average age of employees in a particular department'''