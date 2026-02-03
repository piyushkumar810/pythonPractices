'''
🔹 1. FUNCTION POLYMORPHISM
Same function works with different data types
print(len("Python"))
print(len([1, 2, 3, 4]))
print(len((10, 20)))


📌 len() behaves differently for different objects.
'''



# 🔹 2. OPERATOR OVERLOADING
# Same operator, different meaning
print(10 + 20)           # addition
print("Hello" + "Hi")   # string concatenation


# 📌 + behaves differently based on operands.
# User-Defined Operator Overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)   # 300





# 🔹 3. METHOD OVERRIDING (MOST IMPORTANT)
# Child class redefines parent method
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
d = Dog()

a.sound()
d.sound()
'''
📌 Same method name → different behavior.
Rule:
Same method name
Same parameters
Child method overrides parent method
'''




'''
🔹 4. DUCK TYPING (PYTHON-SPECIFIC)
“If it looks like a duck and quacks like a duck…”
class Laptop:
    def type(self):
        print("Laptop typing")

class Mobile:
    def type(self):
        print("Mobile typing")

def work(device):
    device.type()

work(Laptop())
work(Mobile())


📌 No inheritance needed
📌 Behavior matters, not class type
'''

'''
| Feature        | Overloading  | Overriding   |
| -------------- | ------------ | ------------ |
| When           | Compile-time | Run-time     |
| Python support | ❌            | ✅            |
| Method names   | Same         | Same         |
| Class          | Same         | Parent-child |
'''

'''
5️⃣ Polymorphism with Inheritance
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of circle")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")


📌 Parent reference → child object
📌 Behavior depends on object type
'''