# UNIT–1 : Python Basics & Standard Library
# (Model Question Set – Exam Pattern Based)

# Q1 (a)
# i) How does Python differ from traditional programming languages like C in terms of execution model?
# ii) List any three advantages of using Python.

'''
1- 🔸 C Language
    Uses a compiler
    Entire program is converted into machine code at once
    Errors are shown after compilation
    Output file: .exe
    C source code → Compiler → Machine code → Execution
    
    🔸 Python Language
    Uses an interpreter
    Code is executed line by line
    Errors are shown at runtime
    No separate executable file
    
    Python code → Interpreter → Execution

    
                    ⚠️ EXTRA (FOR CONFIDENT ANSWER)

                        Python is often called:
                        “Interpreted language with bytecode compilation”
                        Because internally:
                        Python source code (.py)
                        Converted to bytecode (.pyc)
                        Bytecode is executed by Python Virtual Machine (PVM)

                        .py → Bytecode → PVM → Output


2-  i)Python has simple and readable syntax, requiring fewer lines of code
    ii)Python provides a large standard library and built-in functions
    iii)Python is easy to debug and maintain due to interpreted execution
'''


# Q1 (b)

# Answer the following:

# i) ________ keyword is used to define a function in Python.
# ii) print("PES", "University", sep="-")
# iii) The ________ operator is used for floor division in Python.
# iv) print(10 | 3)
# v) "10" + 20 (State whether the expression is valid or invalid in Python.)
# vi) print(False == 0)

'''
1- def
2- PES-University
3- //
4- (1011)-11
5- invalid, 
6- True
'''


# Q1 (c)

# Given the following Python code:

# n = 12
# while n > 6:
#     n -= 3
#     print(n)


# i) Find the output of the above code.
# ii) What will be the output if the initial value of n is changed to 7?
# iii) What happens if the statement n -= 3 is removed from the loop?
'''
1- 9,6
2- 4
3- Infinite loop; prints 12 repeatedly
'''

# Q1 (d)

# i) Find the output:

# username = "admin"
# password = "1234"
# is_logged_in = False

# if username == "admin" and (password == "1234" or is_logged_in):
#     print("Login Successful")
# else:
#     print("Access Denied")


# ii) Explain the concept of short-circuit evaluation in Python with respect to logical operators.
'''
1- Login Successful
2- Short-Circuit Evaluation in Python
    Concept Explanation
    
    Short-circuit evaluation means Python stops evaluating a logical expression as soon as the final result is known.
    In Python:
    
    and operator
    Stops if any condition is False
    or operator
    Stops if any condition is True
'''


# Q1 (e)

# Write a Python program that accepts an integer n from the user and prints a pyramid pattern using * characters as shown below.
# (Note: n represents the number of rows.)

# For n = 4, expected output:

#    *
#   ***
#  *****
# *******

n=int(input("enter the row "))
for i in range(1,n+1):
    spaces=(n-i)
    star=(2*i-1)
    print(" "*spaces + "*"*star)
