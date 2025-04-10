
# -------------------if you enter two value
def gcd(a, b):
    while b != 0:
        temp = b
        remainder = a % b
        a = temp
        b = remainder
    return a

# Taking input
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

# Calling function and printing result
result = gcd(a, b)
print("GCD is:", result)
