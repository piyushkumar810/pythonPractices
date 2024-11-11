x=['PwSkills', 'Learner']
for i in x:
    i.upper()
print(x)

# ----------------  sol
# The code doesn't modify the list elements in place because strings are immutable in Python.
#      When you call i.upper(), it returns an uppercase version of the string but doesn't change the 
#      original string i.

# so, output is - ['PwSkills', 'Learner']



print("\n")
# -----------you can use a list comprehension or explicitly assign the uppercase version back to each element. 
x = ['PwSkills', 'Learner']
x = [i.upper() for i in x]
print(x)

# ----or
x = ['PwSkills', 'Learner']
for i in range(len(x)):
    x[i] = x[i].upper()
print(x)