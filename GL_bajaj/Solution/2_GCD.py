
# -------------------if you enter two value
# def gcd(a, b):
#     while b != 0:
#         temp = b
#         remainder = a % b
#         a = temp
#         b = remainder
#     return a

# # Taking input
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))

# # Calling function and printing result
# result = gcd(a, b)
# print("GCD is:", result)


# # ----------------- if you have to find three number GCD
# def gcd(a, b):
#     while b != 0:
#         temp = b
#         remainder = a % b
#         a = temp
#         b = remainder
#     return a

# # Taking input
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))

# # Calling function and printing result
# FirstRes = gcd(a, b)
# result = gcd(FirstRes,c)
# print("GCD is:", result)


# ------------list of numbers
def gcd(a, b):
    while b != 0:
        temp = b
        remainder = a % b
        a = temp
        b = remainder
    return a

# Input list of numbers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate GCD for entire list
current_gcd = nums[0]
for num in nums[1:]:
    current_gcd = gcd(current_gcd, num)

print("GCD of all numbers is:", current_gcd)
