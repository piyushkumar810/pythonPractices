# --------------------------------------how import module work in python
# importing in python is the process of loading code form the pyhton module into the current script

#------------------- 1st way to import all the functionality of math module
# import math
# result= math.sqrt(9)
# print(result)

# ------------------2nd way to import only needed function or variable from math module
# from math import sqrt,pi
# result=sqrt(9)
# print(result)

# -----------------3rd way to import everything(function and variable) from math module
# from math import *
# result=sqrt(9)*pi
# print(result)

# -------------------------------------the use of "as" keyword
import math as mt
result=mt.sqrt(12)
print(result)

# -------------------------------------the dir function
# dir function tells what-what function and variable are used in that module 
print(dir(mt))

# -------------or
# import math
# print(dir(math))