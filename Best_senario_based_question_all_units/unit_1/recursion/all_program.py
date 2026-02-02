

# What is Recursion?
'''
Recursion is a programming technique in which a function calls itself to solve a problem by breaking it into smaller sub-problems.
Every recursive function must have a base condition to stop further function calls.

Syntax of Recursion in Python

def function_name(parameters):
    if base_condition:
        return value
    return function_name(modified_parameters)

'''


# Differentiate between Recursion and Iteration

'''
| Recursion                                                          | Iteration                                          |
| ------------------------------------------------------------------ | -------------------------------------------------- |
| A function calls itself to solve a problem                         | Uses loops (`for`, `while`) to repeat instructions |
| Requires a **base condition** to stop execution                    | Loop condition controls termination                |
| Uses **function call stack**                                       | Does not use function call stack                   |
| Slower due to function call overhead                               | Faster and more memory efficient                   |
| Code is shorter and more readable for problems like tree traversal | Code is simpler for repetitive tasks               |
| Risk of **stack overflow** if depth is large                       | No risk of stack overflow                          |

'''


# What happens if a recursive function does not have a base condition?
'''
Answer:

If a recursive function does not have a base condition, it will call itself indefinitely, 
leading to infinite recursion.This causes a Runtime Error called RecursionError due to
 stack overflow, as each function call occupies memory in the call stack.

Example:
def fun(n):
    return fun(n-1)

Result:
RecursionError: maximum recursion depth exceeded
'''





# ✅ 1️⃣ Count the number of digits in a number (Recursive)
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

num = int(input("Enter number: "))
print("Number of digits:", count_digits(num))

# ✅ 2️⃣ Sum of first n natural numbers (Recursive)
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

n = int(input("Enter n: "))
print("Sum:", sum_natural(n))

# ✅ 3️⃣ Check whether a number is a palindrome (Recursive)
def is_palindrome(num, rev=0, temp=None):
    if temp is None:
        temp = num
    if num == 0:
        return temp == rev
    return is_palindrome(num // 10, rev * 10 + num % 10, temp)

num = int(input("Enter number: "))
print("Palindrome" if is_palindrome(num) else "Not Palindrome")

# ✅ 4️⃣ Find power of a number (xⁿ) (Recursive)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = int(input("Enter x: "))
n = int(input("Enter n: "))
print("Result:", power(x, n))


# ✅ 5️⃣ Count vowels in a string (Recursive)
def count_vowels(s):
    if s == "":
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

string = input("Enter string: ")
print("Vowel count:", count_vowels(string))


# ✅ 6️⃣ Check whether a string is a palindrome (Recursive)
def string_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return string_palindrome(s[1:-1])

s = input("Enter string: ")
print("Palindrome" if string_palindrome(s) else "Not Palindrome")


# ✅ 7️⃣ Remove all spaces from a string (Recursive)
def remove_spaces(s):
    if s == "":
        return ""
    if s[0] == " ":
        return remove_spaces(s[1:])
    return s[0] + remove_spaces(s[1:])

s = input("Enter string: ")
print("Without spaces:", remove_spaces(s))


# 🔥 VERY IMPORTANT (HIGH-PROBABILITY QUESTIONS)
# ✅ 8️⃣ Sum of digits (Recursive)
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))


# ✅ 9️⃣ Factorial of a number (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))
print("Factorial:", factorial(n))

# ✅ 🔟 GCD of two numbers (Recursive – Euclidean method)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))

# ✅ 1️⃣1️⃣ Decimal → Binary (Recursive)
def dec_to_bin(n):
    if n == 0:
        return
    dec_to_bin(n // 2)
    print(n % 2, end="")

num = int(input("Enter decimal number: "))
print("Binary:", end=" ")
dec_to_bin(num)


# ✅ 1️⃣2️⃣ Pascal’s Triangle using Recursion
def pascal(n, r):
    if r == 0 or r == n:
        return 1
    return pascal(n-1, r-1) + pascal(n-1, r)

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print(pascal(i, j), end=" ")
    print()
