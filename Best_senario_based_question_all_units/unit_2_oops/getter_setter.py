'''
1️⃣ Why Getters & Setters Exist
Encapsulation says:
Data should NOT be accessed or modified directly.

So we use:
Getter → to read private data
Setter → to modify private data safely

📌 Primary purpose:
✔ Ensure data encapsulation
✔ Add validation
✔ Avoid direct access to private variables
'''

# 4️⃣ Basic Getter & Setter Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private variable

    # getter
    def get_age(self):
        return self.__age

    # setter
    def set_age(self, age):
        self.__age = age


# 📌 __age is:
# NOT accessed directly
# Accessed via methods only

# 5️⃣ Using Getter & Setter

stud = Student("Dhruv", 14)

print(stud.get_age())   # getter
stud.set_age(16)        # setter
print(stud.get_age())

'''
✔ Controlled access
✔ Encapsulation maintained
'''