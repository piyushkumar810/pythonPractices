# 🔹 PYTHON PATTERN QUESTIONS (ALL TOGETHER)
# Q1. Right-Angled Triangle

# Write a Python program to print the following pattern for a given n:

# *
# **
# ***
# ****
# *****

# ----------------------- solution
n=int(input("enter the row "))
for i in range(1,n+1):
    print("*"*i)



# Q2. Inverted Right-Angled Triangle

# Write a Python program to print:

# *****
# ****
# ***
# **
# *

# ----------------------- solution
n=int(input("enter the row "))
for i in range(1,n+1):
    print("*"*(n-(i-1)))




# Q3. Pyramid Pattern

# Write a Python program to print a pyramid pattern using * for n rows.

# For n = 4:

#    *
#   ***
#  *****
# *******

# ----------------------- solution
n=int(input("enter the row "))
for i in range(1,n+1):
    print("*"*(n-(i-1)))



# Q4. Inverted Pyramid Pattern

# Write a Python program to print the inverted pyramid pattern.

# *******
#  *****
#   ***
#    *




# Q5. Diamond Pattern

# Write a Python program to print a diamond pattern for an odd integer n.

# For n = 5:

#   *
#  ***
# *****
#  ***
#   *

n = 3   # change this to increase size

# Upper part
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

# Lower part
for i in range(n-1):
    print(" " * (i + 1) + "*" * (2*(n - i - 2) + 1))


# Q6. Square Pattern

# Write a Python program to print a square pattern of * for n rows and columns.

# *****
# *****
# *****
# *****
# *****
rows=int(input("enter no of rows"))
for i in range(rows):
    print((rows)* "*")



# Q7. Number Triangle

# Write a Python program to print the following number pattern:

# 1
# 12
# 123
# 1234
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):      # outer loop → rows
    for j in range(1, i + 1):     # inner loop → numbers in each row
        print(j, end="")          # print on same line
    print()                       # move to next line


# Q8. Repeated Number Pattern

# Write a Python program to print:

# 1
# 22
# 333
# 4444
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):      # Outer loop for rows
    for j in range(i):            # Inner loop prints i times
        print(i, end="")          # Print the same number
    print()                       # Move to next line



# Q9. Floyd’s Triangle

# Write a Python program to print Floyd’s triangle for n rows.

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# Q10. Hollow Square Pattern

# Write a Python program to print a hollow square pattern.

# *****
# *   *
# *   *
# *   *
# *****

rows = 5

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
