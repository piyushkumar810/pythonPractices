
'''
🧠 SCENARIO-BASED QUESTION (GETTERS & SETTERS – FULL ENCAPSULATION)
📌 Scenario

You are developing a Student Examination System.
For security and data integrity:
A student’s marks must NOT be accessed or modified directly
Marks must always stay in the range 0 to 100
Any invalid update must be rejected
Marks should be read-only from outside the class

📝 YOUR TASK
1️⃣ Create a class Student
Attributes
name → public
__marks → private

2️⃣ Methods (MANDATORY)
🔹 Getter
get_marks()
Returns student marks
Allows read-only access

🔹 Setter
set_marks(marks)
Updates marks only if:
0 <= marks <= 100
Otherwise:
Print error message
Do NOT update marks

🔹 Display Method
display()
Prints student name and marks (using getter)

⚠️ STRICT EXAM RULES

❌ Do NOT access __marks directly
❌ Do NOT modify marks without setter
✔ Use getter inside display
✔ Apply validation in setter

🔍 Expected Usage
s1 = Student("Piyush", 85)

s1.display()

s1.set_marks(95)
s1.display()

s1.set_marks(120)   # invalid
s1.display()

✅ Expected Output
Name: Piyush
Marks: 85

Marks updated successfully

Name: Piyush
Marks: 95

Invalid marks! Must be between 0 and 100

Name: Piyush
Marks: 95
'''

class Student:
    def __init__(self, name, marks):
        self.name = name          # public attribute
        self.__marks = marks      # private attribute

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully")
        else:
            print("Invalid marks! Must be between 0 and 100")

    # display method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.get_marks())

s1 = Student("Piyush", 85)

s1.display()

s1.set_marks(95)
s1.display()

s1.set_marks(120)   # invalid
s1.display()
