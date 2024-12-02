# 5. Combining AND and OR
# Question: What will the following code output?

a = 0
b = 5
c = a and b or b + 2
print(c)


# Solution:

# a and b: a is 0 (False), so the result is a (0).
# 0 or b + 2: b + 2 is evaluated and returned.
# Output: 7
