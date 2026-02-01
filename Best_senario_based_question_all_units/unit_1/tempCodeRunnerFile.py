
n = int(input("Enter an odd number of rows: "))

# Upper half (including middle)
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

# Lower half
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

