# ----------------------------id function

# q) what is the return type of function id
# Ans --> The id() function in Python returns an integer. This integer represents the memory address
#          of the object passed as an argument to the function.

# ---------------------------or---------------

# In Python, id is a built-in function that returns a unique identifier for a specific object. 
#    This identifier is an integer that represents the memory address where the object is stored 
#    (or an equivalent unique identifier). It helps Python differentiate between different objects, 
#     even if they hold the same values.



a = 5
b = 5
print(id(a))       # Prints an integer (the unique id of a)
print(id(b))       # Same id as `a` because integers are immutable and Python caches small integers
print(a is b)      # True, because `a` and `b` refer to the same object in memory