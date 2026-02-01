# Q1 (a)
# i) How do compilers and interpreters differ in their approach to translating code?
# ii) List any three input devices.
'''
| **Compiler**                                | **Interpreter**                          |
| ------------------------------------------- | ---------------------------------------- |
| Translates the **entire program at once**   | Translates and executes **line by line** |
| Produces a **separate executable file**     | Does **not** produce an executable file  |
| Errors are shown **after full compilation** | Errors are shown **one line at a time**  |
| Execution is **faster** after compilation   | Execution is **slower**                  |
| Example: C, C++                             | Example: Python, JavaScript              |
'''

'''
ii) Any three input devices
Keyboard - Used to enter text and commands
Mouse - Used to point, click, and select items
Scanner - Used to input images or printed documents into a computer
'''

# Q1(B)
# Answer the following:
# i) ________ is a built-in function that is used to determine the type of a Python object.
# ii) print("My", "last", "Exam ", sep="*")
# iii) The ________ operator is used for integer division.
# iv) print(15 & 3)
# v) 7 + 5i (State whether the literal is valid or invalid in Python.)
# vi) print(True == 1)

'''
1- type
2- My*last*Exam
3- //
4- 3

5- Explanation
    In Python, complex numbers use j, not i
    i is not recognized as the imaginary unit

    Therefore, 7 + 5i is an invalid literal in Python , it should be 7+5j


6- ✅ Output: True
    Explanation
    In Python:
    True is treated as 1
    False is treated as 0
'''

# Q1 (c)

# Given the below Python code:
# x = 10
# while x > 5:
#     x -= 2
#     print(x)


# i) Find the output of the code.
# ii) If the initial value of x is changed to 6, what will be the output?
# iii) What happens if the line x -= 2 is removed from the code?

'''
1- 8,6,4
2- situation is this :- when initial value is changed to 6
    x = 6
    while x > 5:
        x -= 2
        print(x)

    output=4    
    
3- Infinite loop; prints 10 repeatedly
'''

# Q1(d)

# i) Find the output:

# name = "PESU"
# age = 50
# is_active = True
# if name == "PESIT" or (name == "PESU" and age <= 30 and is_active):
#     print("Welcome")
# else:
#     print("Access denied")


# ii) Brief the concept of short-circuit evaluation with respect to Python’s logical operators.

'''
Step-by-step evaluation

name == "PESIT" → False
Evaluate the second condition inside brackets:
name == "PESU" → True
age <= 30 → False (50 ≤ 30 ❌)
is_active → True
True and False and True → False

Now:
False or False → False

✅ Output
Access denied


ii) Short-Circuit Evaluation in Python
Concept Explanation

Short-circuit evaluation means Python stops evaluating a logical expression as soon as the final result is known.
In Python:

and operator
Stops if any condition is False
or operator
Stops if any condition is True

Examples
False and print("Hello")   # print() is NOT executed
True or print("Hello")    # print() is NOT executed

Why Python uses short-circuiting
Improves performance
Prevents runtime errors
Avoids unnecessary evaluations
'''

# Q1(e)
# Write a program that takes the number of rows n as input from the user and prints a diamond pattern using asterisks (*) as shown.
# (Note: n is an odd integer.)

# For n = 5, expected output:

#   *
#  ***
# *****
#  ***
#   *


n = int(input("Enter an odd number of rows: "))

# Upper half (including middle)
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

# Lower half
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

