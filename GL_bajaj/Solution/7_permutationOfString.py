# What is a permutation of a string?

'''
   A permutation is a rearrangement of the characters in the string.
   For example, for the string "abc", all possible permutations are:

   abc
   acb
   bac
   bca
   cab
   cba

'''

def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        rest = left + right
        permute(rest, answer + ch)

str=input("enter the string you want : ")
permute(str)


# ---------for better understanding (slicing starts from index 0 and ends at index i-1.)


# str1="length"
# for i in range (len(str1)):
#     print("this is 1st  ",str1[:i])
#     print("this is 2nd  ",str1[i+1:])
#     print("combined = ", str1[:i]+str1[i+1:])
#     print()