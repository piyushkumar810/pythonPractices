# 🔹 UNIT–2
# OOP & Advanced Concepts (Very Important)
# Section A – OOP Programs
'''
Q1.Create a class BankAccount with:
-- Class variable to count accounts
-- Deposit & Withdraw methods
-- Raise exception if balance < minimum
'''
class BankAccount:
    account_count = 0          # Class variable
    minimum_balance = 5000

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.account_count += 1

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        if self.balance - amount < BankAccount.minimum_balance:
            raise ValueError("Minimum balance violation")
        else:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)


# Client code
acc = BankAccount("Piyush", 30000)
acc.deposit(10000)
acc.withdraw(30000)




'''
Q2.Write a Python program to:
Demonstrate method overriding
Use super() explicitly
'''
# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


# Derived class
class Student(Person):
    def __init__(self, name, usn):
        super().__init__(name)     # calling parent constructor
        self.usn = usn

    def display(self):
        super().display()          # calling parent method
        print("USN:", self.usn)


# Client code
s = Student("Piyush", "PESU123")
s.display()



'''
Q3.Create a class Matrix and overload:
+ for matrix addition
== to compare two matrices
'''
'''
like this there are many but few important are:-
__add__()
__eq__()
__lt__()
__gt__()
__le__()
__ge__()
__str__()
__len__()

'''
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    # Overload + operator for matrix addition
    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    # Overload == operator for matrix comparison
    def __eq__(self, other):
        return self.matrix == other.matrix

    def display(self):
        for row in self.matrix:
            print(row)

# Client code
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Matrix addition
m3 = m1 + m2
print("Matrix Addition Result:")
m3.display()

# Matrix comparison
print("Are matrices equal?", m1 == m2)





'''
Q4.Write a program using composition:
Car has Engine
Display engine details via car object
'''
# Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display(self):
        print("Engine type:", self.engine_type)


# Car class (Composition)
class Car:
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine   # Car HAS an Engine

    def display(self):
        print("Car model:", self.model)
        print("Car color:", self.color)
        self.engine.display()  # Access engine via car


# Client code
eng = Engine("Petrol")
car = Car("Kia", "Red", eng)
car.display()




# Section B – Inheritance & Polymorphism
'''
Q5.Create a base class Shape
Derived classes: Rectangle, Circle
Override area() method
Store all objects in a list and compute total area
'''
import math

# Base class
class Shape:
    def area(self):
        return 0


# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):                      # overriding
        return self.length * self.breadth


# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                      # overriding
        return math.pi * self.radius * self.radius


# Client code
shapes = []                              # list to store objects

shapes.append(Rectangle(10, 5))
shapes.append(Circle(7))
shapes.append(Rectangle(4, 6))
shapes.append(Circle(3))

# Compute total area
total_area = 0
for shape in shapes:
    total_area += shape.area()

print("Total Area of all shapes:", total_area)




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
# 10,20

# Q8
class Test:
    def __init__(self):
        print("Init")

    def __del__(self):
        print("Del")

t = Test()
del t
# Init,Del


# ------------------------- question set(pyq)
'''
Q2 (a)
Write an Object-Oriented Program to create a class Complex with img, real and use operator overloading to multiply 
two complex numbers.
formula:-

Real part = ac − bd
Imaginary part = ad + bc
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    # Overload * operator
    def __mul__(self, other):
        real_part = self.real * other.real - self.img * other.img
        img_part = self.real * other.img + self.img * other.real
        return Complex(real_part, img_part)

    def display(self):
        print(f"{self.real} + {self.img}i")


# Client code
c1 = Complex(3, 2)
c2 = Complex(1, 4)

c3 = c1 * c2      # operator overloading

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Multiplication Result:")
c3.display()

    





'''
Q2 (b)

Write an OOP program in Python to create a class to read and add two distances.
Use two member functions get_distance and show_distance
Read and display distance in kms and mts
Use a class variable that counts the different values stored
Use add_distance to add distances
'''
class Distance:
    count = 0   # class variable

    def __init__(self):
        self.km = 0
        self.m = 0
        Distance.count += 1

    def get_distance(self):
        self.km = int(input("Enter kilometers: "))
        self.m = int(input("Enter meters: "))

    def add_distance(self, other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        total_km += total_m // 1000
        total_m = total_m % 1000

        result = Distance()
        result.km = total_km
        result.m = total_m
        return result

    def show_distance(self):
        print(f"{self.km} kms {self.m} mts")


# Client code
d1 = Distance()
d1.get_distance()

d2 = Distance()
d2.get_distance()

d3 = d1.add_distance(d2)

print("First Distance:")
d1.show_distance()

print("Second Distance:")
d2.show_distance()

print("Total Distance:")
d3.show_distance()

print("Total Distance objects created:", Distance.count)





'''
Q2 (c)
Write an Object-Oriented program in Python to create a class called person with data members name and age.
Create an inherited class employee with data member department.

Check whether a given person is an employee or not

Display the average age of employees in a particular department
'''

# ✅ OOP Program: Person → Employee (Inheritance + isinstance + Aggregation)
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Derived class
class Employee(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


# Client code
people = []

# Creating objects
people.append(Person("Piyush", 20))
people.append(Employee("Rahul", 30, "HR"))
people.append(Employee("Anita", 25, "IT"))
people.append(Employee("Suresh", 35, "HR"))
people.append(Person("Ravi", 40))

# Check whether a given person is an employee
for p in people:
    if isinstance(p, Employee):
        print(p.name, "is an Employee")
    else:
        print(p.name, "is NOT an Employee")

# Calculate average age of employees in a particular department
dept = input("Enter department to find average age: ")

total_age = 0
count = 0

for p in people:
    if isinstance(p, Employee) and p.department == dept:
        total_age += p.age
        count += 1

if count > 0:
    print("Average age of employees in", dept, "department:", total_age / count)
else:
    print("No employees found in this department")