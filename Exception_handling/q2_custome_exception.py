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