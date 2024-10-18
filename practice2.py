# ------------------------------------problem is init() variable are easily accessed anywhere inside the class but course method variable are not accessed why ?


# ---------------------------wrong program
# class parentclass:
#     def __init__(self):
#         self.name="piyush"
#         self.roll=28

#     def course(self):
#         self.course="BCA"

#     def show(self):
#         print(f"the name of student is {self.name} and roll no is {self.roll} and the course he is applied for {self.course}")

# obj1=parentclass()
# obj1.show()


# -----------------------wright solution
class parentclass:
    def __init__(self):
        self.name = "piyush"
        self.roll = 28

    def course(self):
        self.course = "BCA"  # Set course here

    def show(self):
        if hasattr(self, 'course'):  # Check if self.course exists
            print(f"The name of the student is {self.name}, roll no is {self.roll}, and the course applied for is {self.course}.")
        else:
            print("Course is not set.")

# Usage
obj1 = parentclass()
obj1.course()  # Call course() to set the course
obj1.show()


# ------------------------------------or

# class parentclass:
#     def __init__(self):
#         self.name="piyush"
#         self.roll=28

#     def course(self):
#         self.course="BCA"

#     def show(self):
#         self.course()
#         print(f"The name of the student is {self.name}, roll no is {self.roll}, and the course applied for is {self.course}.")

# obj1=parentclass()
# obj1.show()