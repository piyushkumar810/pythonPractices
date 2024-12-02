# 4. Default Values with OR
# Question: What is the value of name?

user_input = ""
default = "Guest"
name = user_input or default
print(name)


# Solution:

# user_input is an empty string (evaluates to False), so default is returned.
# Output: Guest