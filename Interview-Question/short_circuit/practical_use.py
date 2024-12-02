# Practical Use of Short-Circuiting in Python

# Short-circuiting is often used for:
# 1st -> Avoiding unnecessary computation:

a = [1, 2, 3]
if a and a[0] == 1:  # Only checks a[0] if a is not empty
    print("Condition met")


# 2nd -> Default values with or:

user_input = ""
default = "Guest"
name = user_input or default
print(name)  # Output: Guest