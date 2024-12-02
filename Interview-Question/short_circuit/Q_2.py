a = None
b = "Python"

result = a or b
print(result)


# Explanation:

# The first operand (a) is None, which evaluates to False.
# Since or short-circuits when the first operand is False, it immediately evaluates the second operand (b) and returns it.

# Output: Python.
