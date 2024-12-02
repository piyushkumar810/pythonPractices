# 8. Avoiding Index Errors
# Question: What will happen?

a = []
if a and a[0] == 1:
    print("First element is 1")
else:
    print("List is empty or first element is not 1")


# Solution:

# a is empty, so a and a[0] == 1 short-circuits at a and skips the invalid index access.
# Output: List is empty or first element is not 1
