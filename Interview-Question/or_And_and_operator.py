# In Python, the or and and operators are logical operators used to combine conditional statements:

# -----------------------------------and Operator:

# Returns True only if both conditions are True.
# If either condition is False, it returns False.
# Example:

x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive")


# ------------------------------------or Operator:

# Returns True if at least one of the conditions is True.
# Only returns False if both conditions are False.
# Example:

x = -5
y = 10
if x > 0 or y > 0:
    print("At least one of x or y is positive")
print("\n")



# ------------------but----------but------------------but-------------

# When you use or and and operators directly with values (not in a conditional),they behave a bit differently:
# eg

x=9
y=41
print(x or y, x and y) 
print("\n")

# here 
# 'or' will return -> first true value (true values are non zero, non empty, non None (0,[],None --> these are not considered as triee value)) 
# eg 1
a=0
b=5
print(a or b)

# eg 2
a1=0
b1=0
print(a1 or b1)
# output 0 --> because if he not get's true value then it returns last value means b1

# eg 3
a2=7
b2=5
print(a2 or b2)
print("\n")

# 'and' will return-> first false value
# eg1
a3=0
b3=5
print(a3 and b3)

# eg2
a4=7
b4=5
print(a4 and b4)