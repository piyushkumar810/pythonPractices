# --------------------Q 1. Logical AND Behavior

# Question: What will be the output of the following code?
a = 0
b = 10
result = a and b
print(result)

# Solution:

# a is 0 (evaluates to False), so and short-circuits and returns a.
# Output: 0


# ---------------------Q 2. Logical OR Behavior

a = None
b = "Python"
result = a or b
print(result)


# Solution:

# a is None (evaluates to False), so or short-circuits and returns b.
# Output: Python
