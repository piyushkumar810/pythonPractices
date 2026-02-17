# 🔹 UNIT–1
# Python Basics & Standard Library (Tough Level)

# Section A – Programs (8–10 marks type)
'''
1.Write a Python program using procedural approach to:
   Accept a range
   Print numbers where sum of digits is divisible by 3
   Count how many such numbers exist
'''
# Accept range from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("\nNumbers whose sum of digits is divisible by 3:\n")

# Loop through the range
for num in range(start, end + 1):
    temp = num
    digit_sum = 0

    # Calculate sum of digits
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    # Check divisibility by 3
    if digit_sum % 3 == 0:
        print(num)
        count += 1

# Print total count
print("\nTotal count:", count)


'''
2.Write a user-defined function to:
    Check whether a string is a rotational palindrome
    Return the number of rotations needed
'''
'''
3.Write a recursive program to:
    Convert a decimal number to binary
    Print the binary digits in correct order
'''
'''
4.Write a Python program to:
    Accept a list of integers
    Remove duplicates without using set
    Preserve original order
'''

# Section B - Comprehensions & Iterators
'''
5.Write list comprehensions to:
    Extract all vowels from a sentence
    Reverse words having even length
'''
'''
6.Generate (number, cube) pairs for numbers divisible by 4
    Write a dictionary comprehension to:
    Map each word to its frequency
    Ignore case sensitivity
'''
'''
7.Create a custom iterator that generates:
    Prime numbers up to n
    Stops iteration using StopIteration
'''

# Section C – Output Based (MCQ / 1–2 marks)
# Q8
x = [i*i for i in range(5) if i%2]
print(x)


#Q9
def f(a, b=[]):
    b.append(a)
    return b

print(f(1))
print(f(2))

#Q10
from collections import Counter
c = Counter("programming")
print(c['m'])


# ------------------------ qustion set
'''Q1(a)

Write Python Program using Procedural programs to:
Find all numbers that are divisible by both 5 and 7 within a given range.
Reverse a given string using user defined function.
'''

'''
Q1 (b)

Write list comprehensions to:
Print the first and last letter of every name in a list.
Print a list of strings in uppercase.
Print the reverse of each name in a list.
'''

'''Q1 (c)

Write a recursive program to:
Calculate sum of the digits of a number.
Print Pascal’s triangle up to n rows.
'''

'''
Q1 (d)

Find the output:

words = ["music", "analysis", "soul"]
s = [len(word) for word in words]
print(s)
'''