# 🧠 What is a Custom Exception?
'''
A custom exception is an error you define yourself to represent a specific problem in your program.

Python already has:
ValueError
IndexError
ZeroDivisionError

But sometimes they are not expressive enough.
📌 Example problem:
Age entered is negative
Password is too weak
Marks are out of range

Python has no built-in exception for these → we create our own

🔑 Core Rule (Must Remember)
Custom exceptions are created by inheriting from Exception class

🧪 Basic Syntax (EXAM IMPORTANT)
class MyError(Exception):
    pass


✔️ class
✔️ Inherits from Exception
✔️ pass means no extra code

🧩 Example 1: Age Validation (Simple & Clear)
❌ Problem
'''
# Age cannot be negative or above 120.

# ✅ Custom Exception
class InvalidAgeError(Exception):
    pass

# ✅ Using the Custom Exception
def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age entered")
    else:
        print("Age is valid")

try:
    age = int(input("Enter age: "))
    check_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a number")

'''
🔍 How Execution Works

User enters age
check_age() checks condition
raise InvalidAgeError → error occurs
Control jumps to except InvalidAgeError
Message is printed
'''




# ---------------------------------------- example 2
# 🧪 Example 2: Marks Validation (Exam-Level)
# ❌ Rule

# Marks must be between 0 and 100.
class InvalidMarksError(Exception):
    pass

def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    return marks

try:
    m = int(input("Enter marks: "))
    print("Marks entered:", check_marks(m))
except InvalidMarksError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Invalid input")





# --------------------------------------- example 3
# 🧪 Example 3 (TRICKY): finally still runs
class LowBalanceError(Exception):
    pass

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise LowBalanceError("Insufficient balance")
        print("Withdraw successful")
    finally:
        print("Transaction completed")

try:
    withdraw(1000, 2000)
except LowBalanceError as e:
    print(e)


'''
Output:
Transaction completed
Insufficient balance


🔥 finally runs even with custom exceptions

🚨 EXAM TRAPS (VERY IMPORTANT)
❌ Wrong
class MyError:
    pass


❌ Does NOT inherit from Exception

❌ Wrong
raise "Error"


❌ Only exception objects allowed

✅ Correct
raise MyError("message")
'''