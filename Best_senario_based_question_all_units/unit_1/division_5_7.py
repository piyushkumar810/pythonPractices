# Write Python Program using Procedural programs to:
# Find all numbers that are divisible by both 5 and 7 within a given range.
# Reverse a given string using user defined function.

def division():
    start=int(input("enter the starting range: "))
    end=int(input("enter the ending range: "))

    print("the numbers divisble by 5 and 7 are: ")
    for i in range(start,end+1):
        if(i%5==0 and i%7==0):
            print(i)

def string_reverse():
    user_string=input("enter the string :")
    new_str=user_string[::-1]
    print(new_str)

division()
string_reverse()
