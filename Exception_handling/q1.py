# 🧪 Coding Question 1 (Very Important)
'''
Write a Python program that:

Takes two integers from the user
Performs division
Handles:
ZeroDivisionError
ValueError
Uses finally to print "Execution completed"
If no exception occurs, print "Division successful"

🔍 Expected Concepts
try / except / else / finally
multiple exceptions
clean control flow
'''

def handling(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("cannot divide by zero")
    except ValueError:
        print("value error")
    else:
        print("division sucessful")
    finally:
        print("Execution completed")

input_a=int(input("enter tha value"))
input_b=int(input("enter tha value"))
print(handling(input_a,input_b))


# ----------------- little correction in this code
def handling(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Division successful:", result)
    finally:
        print("Execution completed")

try:
    input_a = int(input("Enter first value: "))
    input_b = int(input("Enter second value: "))
    handling(input_a, input_b)
except ValueError:
    print("Invalid input")




# Question 2
'''
Write a function safe_access(lst, index) that:
Returns the element at the given index
If the index is invalid, return "Index out of range"
Uses try-except
Must not crash
Do not use if index >= len(lst)

🔍 Expected Concepts
IndexError handling
defensive programming
clean exception handling
'''

def safe_access(lst, index):
    try:
        result=lst[index]
    except IndexError:
        print("index out of bound")

lst=[10,20,30]
index=int(input("enter the eindex"))
print(safe_access(lst,index))


# ------------ little correction
def safe_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

lst = [10, 20, 30]
index = int(input("Enter the index: "))
print(safe_access(lst, index))
