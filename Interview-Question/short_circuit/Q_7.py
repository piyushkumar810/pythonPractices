# 6. Evaluating Truthy and Falsy
# Question: What will be printed?

values = [0, "", None, "Python"]
result = next(v for v in values if v)
print(result)


# Solution:

# The generator evaluates each value in values. The first truthy value is "Python".
# Output: Python