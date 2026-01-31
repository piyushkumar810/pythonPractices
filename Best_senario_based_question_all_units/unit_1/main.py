# Write a user-defined function to:

# Check whether a string is a rotational palindrome

# Return the number of rotations needed
# String: "aab"
# Rotations:
# 0 → aab   (not palindrome)
# 1 → aba   (palindrome ✅)

# ✅ Exam Tip (remember this line)

# .split() → words
# list(string) → characters

def rotational_pallindrom(str1):
    rotation_count=0
    splitted_string=list(str1)
    print(splitted_string)
    for i in range(len(splitted_string)-1):
        new_string=splitted_string[1: ]+splitted_string[0]
        print(new_string)
        
        

str1=input("enter a string ")
rotational_pallindrom(str1)