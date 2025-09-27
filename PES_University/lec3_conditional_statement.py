# ------------------------------------------ conditional statement
# print("---------------------conditional statement-----------------------")
# print("--- 1. if statement---")
# print("q1. given a number check if it a negative number")
# num1=int(input("enter a number"))
# if num1<0:
#     print("number is negative")


# print()
# print()
# print("--- 2. if-else statement---")
# print("q2. given a number check it is even or odd")
# num2=int(input("enter a number"))
# if (num2 %2==0):
#     print(f"the given number {num2} is even")
# else:
#     print(f"the given number {num2} is odd")


# print()
# print("q3. given a number check whether it is even or odd and if it is even check is it divisible by 5 if its an odd number check it is divisible by 6")
# num3=int(input("enter a number"))
# if (num3 %2==0):
#     if (num3 % 5==0):
#         print(f"yes given number {num3} is even as well as divisible by 5")
#     else:
#         print(f"yes given number {num3} is even but not divisible by 5")
# else:
#     if(num3%6==0):
#         print(f"yes given number {num3} is odd as well as divisible by 6")
#     else:
#         print(f"yes given number {num3} is odd but not divisible by 6")



# print()
# print("--- 2. if-else statement---")

# print()
# print("--- 3. elif statement---")

# print()
# print("--- 4. elif ladder statement---")

# print()
# print("--- 5. nested if statement---")

# print()
# print("--- 5. match case statement---")


# ----------------------------------------- looping statement -------------------------------
# print()
# print("------------------------ looping statement-----------------------")
# print("---for loop---")
# for i in range(10,0,-1):
#     print(i)

# for i in range(0,10,-1):
#     print(i)

# for i in range(10,0,1):   # it will run and the output is (nothing) , but it will not give any error
#     print(i)

# for i in range(10,2):     # When step is not given, default = +1. output will again nothing
#     print(i)

# for i in range(5,15):
#     print(i)

# for i in range( ,10,2):    #This is a syntax error because you left the first parameter blank.
#     print(i)

# for loop also allows me to use else statement inside the for loop
# for i in " ":
#     print(i) 
# else:
#     print(i)


# print()
# print("---while loop---")

# print("q1. given a number a display its multiplacation tabe 1-10 using loops diplay the no wheree each havine 1-10 inside that 1-10")
# for i in range(1,11):
#     print(f"1*{i}={i}")


# for i in range(1,11):
#     print(i)
#     for i in range(1,11):
#         print(i)

# print("q2. given the no n display the sum of all no till n")
# num5 = int(input("Enter the number: "))
# for i in range(1, num5 + 1):
#     print(i)

# q4. sum of numbers until the sum exceeds 150.
# total = 0
# num = 1
# while total <= 150:
#     total += num
#     num += 1
# print("The sum exceeded 150. Final sum:", total)
# print("Last number added:", num - 1)


# q5. WAP to display whetehr the given no is a prime no or not.
# num_one=int(input("enter the number :"))
# counter=2
# flag=0
# while counter <=(num_one/2):
#     if(num_one%counter==0):
#         flag=1
#         break
#     counter+=1
# if(flag==0):
#     print(f"{num_one} is a prime number")
# else:
#     print(f"{num_one} is not a prime number")

# q6. give a list of 20 number[] display the numbers if they are even if they are odd skip it.
list1=[1,2,2,1,4,6,7,8,10,2,10]
for list in list1:
    if(list%2==0):
        print(list)
    else:
        continue
print()

# q7. read a name and diplay the name character by character.
name="piyush kumar"
for nam in name:
    print(nam)
print()

# q8. given a number display all the prime numbers that are between 1 and 10
for num in range(1,11):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)