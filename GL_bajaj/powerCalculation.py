# power calculation

def powerCal(a, b):
    print("base =", a)
    print("power =", b)

    # Case: base is 0
    if a == 0:
        if b == 0:
            return "Your result is undefined or 1"
        elif b > 0:
            return "Your result is 0"
        else:
            return "You gave exponent in negative with base 0 – result is undefined (division by zero)"

    # Case: base is not 0
    res = 1
    if b == 0:
        return "Your result is 1"
    elif b > 0:
        for _ in range(b):
            res *= a
        return f"Your result is {res}"
    else:  # b < 0
        for _ in range(-b):
            res *= a
        return f"Your result is {1/res}"  # Return reciprocal for negative exponents

# Take input from user
base = int(input("Enter the base value: "))
exponent = int(input("Enter the power value: "))

# Call the function and print result
result = powerCal(base, exponent)
print(result)


# -----------------------------------easy way to handle all the cases
import math

def powerCal(a, b):
    print("base =", a)
    print("power =", b)

    # Case: base is 0
    if a == 0:
        if b == 0:
            return "Your result is undefined or 1"
        elif b > 0:
            return "Your result is 0"
        else:
            return "Undefined: division by zero"

    # Now handling all cases, including fractions
    try:
        result = a ** b  # Handles positive, negative, and fractional powers
        return f"Your result is {result}"
    except ValueError:
        return "Error: Result is a complex number (e.g., negative base with fractional exponent)"
    except ZeroDivisionError:
        return "Error: Division by zero"

# Take input from user
base = float(input("Enter the base value: "))
exponent = float(input("Enter the power value: "))

# Call the function and print result
result = powerCal(base, exponent)
print(result)
