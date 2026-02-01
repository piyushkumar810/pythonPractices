# Write a recursive program to:
# Calculate sum of the digits of a number.
# Print Pascal’s triangle up to n rows.

def sum_of_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digits(num // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))


# -------------------- pascal triangle vvi
n = int(input("Enter number of rows: "))

for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
