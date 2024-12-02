# Short-Circuit to Avoid Errors
# Question: What will happen here?

x = 0
if x != 0 and (10 / x > 1):
    print("True")
else:
    print("False")


# Solution:

# x != 0 is False, so the second condition (10 / x > 1) is not evaluated, avoiding a ZeroDivisionError.
# Output: False