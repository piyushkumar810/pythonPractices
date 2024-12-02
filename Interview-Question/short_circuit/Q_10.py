# 9. Combining Logical Operators
# Question: Predict the output:

a, b, c = 0, 1, 2
result = a or (b and c)
print(result)


# Solution:

# b and c: Both are truthy, so c is returned.
# a or c: a is 0, so c is returned.
# Output: 2
