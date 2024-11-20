def strong_number(n):
    sum = 0
    original_no = n  # Preserve the original number

    while n != 0:
        digit = n % 10
        n = n // 10

        factorial = 1
        temp = digit
        while temp >= 1:
            factorial *= temp
            temp -= 1

        sum += factorial

    return sum

# Input from the user
n = int(input("Enter the number you want to check: "))
result = strong_number(n)

# Compare the result with the original number
if n == result:
    print(f"Yes, {result} is a strong number.")
else:
    print(f"No, {result} is not a strong number.")
