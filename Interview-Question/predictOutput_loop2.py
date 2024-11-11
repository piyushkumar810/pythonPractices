# Q) the 'else' keyword can be used with :
# a) if            b)elif          c)for          d)while        e)All

# ----------------sol
# else can be used with all

# 1. if and elif statements
# The else keyword is used to specify a block of code that runs if the condition in the if or elif statements is not met.

x = 5

if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")


print("\n")

# 2. for loop with else
# The else block in a for loop runs after the loop finishes iterating over all items, but it does not run if the loop is exited with a break statement.

for i in range(5):
    print(i)
else:
    print("Loop completed without break")


print("\n")

# 3. while loop with else
# Similarly, the else block in a while loop runs after the loop finishes naturally (when the condition becomes False), but it does not run if the loop is exited by a break.

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop ended without break")

print("\n")
# Example with break
count = 0
while count < 3:
    if count == 2:
        break
    print(count)
    count += 1
else:
    print("Loop ended without break")  # This won't print