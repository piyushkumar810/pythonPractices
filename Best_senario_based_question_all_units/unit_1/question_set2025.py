# Q1(A)
# Answer the following:

# i) ________ function is used to read input from the user in Python.

# ii) What is the output?
#     print(type(10.5))


# iii) The ________ operator is used to check membership in Python.

# iv) Find the output:
#     print(7 << 1)

# v) [1, 2, 3] + [4, 5]
#    (State whether the expression is valid or invalid.)

# vi) Find the output:
#     print(bool(""))

'''
1- input()
2- <class 'float'>
3- in

4- Explanation (exam-oriented)
    << is the left shift operator
    It shifts all bits one position to the left
    Left shifting by 1 is equivalent to multiplying by 2
    
    Binary representation:
    
    7 → 111
    7 << 1 → 1110 (binary)
    1110₂ = 14₁₀

    output-14

5- Valid
    Reason: List concatenation is allowed.

6- False

'''


# Q1(B)
# *
# **
# ***
# ****
# *****

n=int(input("enter the row "))
for i in range(1,n+1):
    print("*"*i )


# Q1(C)
# i) Difference between Syntax Error and Runtime Error
'''
Syntax Error
Occurs due to incorrect grammar of Python
Detected before execution
Example: missing : or wrong indentation

Runtime Error
Occurs during execution
Program runs but fails due to illegal operation
Example: division by zero
'''
# ii) Any three features of Python
'''
Simple and easy-to-learn syntax
Interpreted and platform-independent
Large standard library support
'''

# Q1(D)
x = 0

if x and print("Hello"):
    print("Yes")
else:
    print("No")
'''
output - NO

Explanation (Short-Circuit Evaluation)
x is 0 → treated as False
In and, if the first condition is False, Python stops evaluation
print("Hello") is never executed
'''