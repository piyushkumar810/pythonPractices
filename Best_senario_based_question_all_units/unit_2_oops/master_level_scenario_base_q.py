'''
🧠 MASTER SCENARIO: Smart University Management System
📌 Scenario
A university wants to build a Smart University System to manage people and their payments securely.
There are two types of users:
Person (base entity)
Student (specialized entity)
The university wants:
Sensitive data hidden
Controlled access
Reusability
Clean design

🧱 SYSTEM REQUIREMENTS
🔹 1️⃣ Parent Class: Person
Attributes
name → public
__age → private

Methods
get_age() → returns age
set_age(age)
age must be > 0
display_info()
prints name and age

🔹 2️⃣ Child Class: Student(Person)
Additional Attributes
student_id → public
__fees → private
Constructor Rules
Use super() to initialize name and age
Initialize student_id and __fees

🔹 3️⃣ Student Methods (ALL REQUIRED)
🔐 Encapsulation
get_fees() → returns fees
pay_fees(amount)
amount must be positive
amount must not exceed fees

🔁 Method Overriding
Override display_info()
Show:
name
age
student_id
remaining fees

🔍 STRICT RULES (EXAM CRITICAL)

❌ No direct access to __age
❌ No direct access to __fees
❌ Child must NOT redefine parent data
✔ Use getters & setters
✔ Use super()
✔ Validation is mandatory

🧪 EXPECTED USAGE (VERY IMPORTANT)
s1 = Student("Piyush", 20, "PES123", 50000)

s1.display_info()

s1.pay_fees(20000)
print("Remaining Fees:", s1.get_fees())

s1.set_age(21)
s1.display_info()

s1.pay_fees(40000)   # should show error

✅ EXPECTED OUTPUT (LOGIC-WISE)
Name: Piyush
Age: 20
Student ID: PES123
Fees Due: 50000

Fees paid: 20000
Remaining Fees: 30000

Age updated to 21
Name: Piyush
Age: 21
Student ID: PES123
Fees Due: 30000

Payment exceeds remaining fees
'''