# In Python, the underscore _ in a for loop like:

# for _ in range(-b):
# is just a convention that means:
# “I don’t care about the loop variable.”

# 🔍 Normally:
# When you write:

for i in range(5):
    print(i)
    
# You're using i to track the loop index (0, 1, 2, ...).

# ✅ But with _:
# If you don’t need to use the variable inside the loop, you can just use _ to make that clear.

# Example:

res = 1
for _ in range(3):  # loop runs 3 times, but we don't use the loop variable
    res *= 2

# This improves readability — it tells other developers:
"I'm looping a number of times, but I don't need the counter itself."