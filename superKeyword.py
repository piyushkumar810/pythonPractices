# -------------------------------------super keyword in pyhton
# super() keyword in python is used to refer the parent class.

# let's see example

# --------------wrong program
# class parentclass:
#     def student(self):
#         self.name="piyush"
#         self.roll=28

#     def course(self):
#         self.course="BCA"

#     def show(self):
#         print(f"the name of student is {self.name} and roll no is {self.roll} and the course he is applied for {self.course}")

# class childclass(parentclass):
#     def college(self):
#         self.college="vinobha bhave university" 

#     def showDetails(self):
#         print(f"This is {self.college}")
#         super().show()

# obj1=childclass()
# obj1.showDetails()


# ----------------------------problem
# The code you've written demonstrates inheritance in Python, where the childclass inherits from 
# the parentclass. However, there is an issue when you call showDetails(). It will raise an
#  AttributeError because the student() and course() methods are never explicitly called to 
# initialize the name, roll, and course attributes.

# To fix this, you should either:

# Call student() and course() inside the childclass methods.
# Or initialize those attributes in the constructor (__init__).


# ----------------------------solution
class ParentClass:
    def student(self):
        self.name = "Piyush"
        self.roll = 28

    def course(self):
        self.course = "BCA"

    def show(self):
        print(f"The name of student is {self.name}, roll no is {self.roll}, and the course he is applied for is {self.course}.")

class ChildClass(ParentClass):
    def __init__(self):
        self.student()  # Initialize student info
        self.course()   # Initialize course info

    def college(self):
        self.college = "Vinobha Bhave University" 

    def showDetails(self):
        self.college()  # Initialize college info
        print(f"This is {self.college}")
        super().show()  # Call the parent class show method

obj1 = ChildClass()
obj1.showDetails()