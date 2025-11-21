
# ----------- first way

# 📌 Example 1: Change class variable using class name (Correct way)
class A:
    x = 10  # class variable

print(A.x)   # 10
A.x = 50     # change class variable
print(A.x)   # 50


#---------------------- second way

# 📌 Example 2: Changing class variable using object (Wrong way)
class A:
    x = 10

obj1 = A()
obj1.x = 100
print(A.x)     # 10  (Not changed)
print(obj1.x)  # 100 (New instance variable created)
'''❌ This does not change the class variable.
It creates a new instance variable only for obj1.'''

# ---------------------third way

# 📌 Example 3: Changing class variable using classmethod (Correct way)
class A:
    x = 10

    @classmethod
    def update_x(cls, value):
        cls.x = value

A.update_x(200)
print(A.x)   # 200



# 📌 Example 4: All objects share updated class variable
class A:
    x = 5

obj1 = A()
obj2 = A()

A.x = 20

print(obj1.x)  # 20
print(obj2.x)  # 20


# ✔ All objects see the updated value.
