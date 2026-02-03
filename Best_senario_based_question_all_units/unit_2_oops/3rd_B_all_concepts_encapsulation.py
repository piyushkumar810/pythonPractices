'''
🧠 HARD Scenario: Encapsulation + Inheritance (Code)
📌 Scenario
You are designing a Secure Employee Payroll System for a company.
There are two types of employees:
Employee (general)
Manager (specialized employee)

🧱 RULES (VERY IMPORTANT)
Salary must be PRIVATE and never accessed directly
Salary must be modified only through methods
Manager gets bonus in addition to salary
Bonus calculation must not expose salary
Use inheritance correctly
Use super() properly

📝 YOUR TASK
1️⃣ Create Parent Class Employee
Attributes:
name → public
__salary → private

Methods:
get_salary() → returns salary
set_salary(amount)
amount must be positive
display_info() → prints employee name and salary

2️⃣ Create Child Class Manager(Employee)
Additional Attribute
bonus → public
Additional Method
total_income()
returns salary + bonus
MUST use parent methods (no direct access to __salary)

⚠️ STRICT EXAM CONSTRAINTS

❌ Do NOT use self.__salary inside Manager
❌ Do NOT redefine salary in child class
✔ Use super()
✔ Use encapsulation strictly

🔍 Expected Usage
m1 = Manager("Piyush", 50000, 10000)

m1.display_info()
print("Total Income:", m1.total_income())

m1.set_salary(60000)
print("Total Income:", m1.total_income())

m1.set_salary(-2000)   # should give error

✅ Expected Behavior
Employee Name: Piyush
Salary: 50000
Total Income: 60000
Salary updated to 60000
Total Income: 70000
Salary must be positive

🎯 WHAT THIS QUESTION TESTS
True encapsulation (private data)
Inheritance without breaking encapsulation
Correct use of super()
Method-based data access
Real-world design thinking
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount <= 0:
            print("Salary must be positive")
        else:
            self.__salary = amount
            print(f"Salary updated to {self.__salary}")

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_income(self):
        return self.get_salary() + self.bonus
    

m1 = Manager("Piyush", 50000, 10000)

m1.display_info()
print("Total Income:", m1.total_income())

m1.set_salary(60000)
print("Total Income:", m1.total_income())

m1.set_salary(-2000)