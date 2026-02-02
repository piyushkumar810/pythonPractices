'''
🧠 Scenario-Based Question: Inheritance (Code)
📌 Scenario

You are developing a University Person Management System.
There are two types of people:
Person (general)
Student (specialized)

📝 Your Task
1️⃣ Create a Parent class Person
Attributes:
name
age
Methods:
display_info() → prints name and age

2️⃣ Create a Child class Student that inherits from Person
Additional attribute:
student_id
Additional method:
display_student() → prints name, age, and student_id

3️⃣ Important Rules (EXAM CONDITIONS)
Use super() to initialize parent attributes
Do NOT repeat parent attributes in child
Use proper dot notation
Follow correct constructor order

🔍 Expected Usage
s1 = Student("Piyush", 20, "PES123")

s1.display_info()
s1.display_student()

✅ Expected Output
Name: Piyush
Age: 20
Student ID: PES123
'''

class Person:
    def __init__(self, name , age):
        self.name=name
        self.age=age

    def display_info(self):
        print(f"person name is : {self.name} and his age is : {self.age}")

class Student(Person):
    def __init__(self, name , age, student_id):
        self.student_id=student_id
        super().__init__(name,age)
    
    def display_student(self):
        print(f"student name : {self.name} his age is : {self.age} and his id is : {self.student_id}")

s1=Student("Piyush", 20, "PES123")

s1.display_info()
s1.display_student()