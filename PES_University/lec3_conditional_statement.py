# ------------------------------------------ conditional statement
print("---------------------conditional statement-----------------------")
print("--- 1. if statement---")
print("q1. given a number check if it a negative number")
num1=int(input("enter a number"))
if num1<0:
    print("number is negative")


print()
print()
print("--- 2. if-else statement---")
print("q2. given a number check it is even or odd")
num2=int(input("enter a number"))
if (num2 %2==0):
    print(f"the given number {num2} is even")
else:
    print(f"the given number {num2} is odd")


print()
print("q3. given a number check whether it is even or odd and if it is even check is it divisible by 5 if its an odd number check it is divisible by 6")
num3=int(input("enter a number"))
if (num3 %2==0):
    if (num3 % 5==0):
        print(f"yes given number {num3} is even as well as divisible by 5")
    else:
        print(f"yes given number {num3} is even but not divisible by 5")
else:
    if(num3%6==0):
        print(f"yes given number {num3} is odd as well as divisible by 6")
    else:
        print(f"yes given number {num3} is odd but not divisible by 6")



print()
print("--- 2. if-else statement---")

# print()
# print("--- 3. elif statement---")

# print()
# print("--- 4. elif ladder statement---")

# print()
# print("--- 5. nested if statement---")

# print()
# print("--- 5. match case statement---")