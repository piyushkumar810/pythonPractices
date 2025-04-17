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