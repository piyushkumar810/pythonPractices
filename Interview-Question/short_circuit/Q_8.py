# 7. Using Short-Circuit in Functions
# Question: What is the output?

def check_value(x):
    return x > 0

print(0 and check_value(1))
print(1 or check_value(1))


# Solution:

# 0 and check_value(1): 0 short-circuits the function call, so False.
# 1 or check_value(1): 1 short-circuits, so True.
# Output: 0, 1
