# ------------------------------------Decision making statement in python

#------------------------ if-statement

# Q) 18+ age will vote
n=int(input("Enter your age : "))
print("your age is: ", n)
if(n>18):
    print("your are eligable for voting ")
if(n<18):
    print("grow up for voting")

# ----------------------if-else statement

# Q)accept a value and divide it by 7 if remainder will greater than quotient then find square of the value otherwise find cube of the remiander
print("\n") 
m=int(input("Enter any number : "))
print("your  entered number is : ", m)
q=m/7
r=m%7
if(r>q):
    print("reminder is greater : ",r*r)
else:
    print("quotiant is greater : ",q**3)

# -------------------------elif statement

# Q) accept a mark which is obtained in the examand find the grade obtained
print("\n")
mark=int(input("Enter your mark obtained out of 500 : "))
if(mark>=450 and mark<500):
    print("outstanding performance👌")
elif(mark>=350 and mark<450):
    print("good👍")
elif(mark>=250 and mark<350):
    print("pass🤞")
else:
    print("fail🤦‍♂️")

# ---------------------------nested if-else statement

# Q)accept 3 value and find greatest among them
print("\n")
num1=int(input("Enetr first value : "))
num2=int(input("Enetr second value : "))
num3=int(input("Enetr third value : "))

g=num1
if(num1>num2):
    if(num1>num3):
        g=num1
    else:
        g=num3
else:
    if(num2>num3):
        g=num2
    else:
        g=num3
print("the greatest value among three is : ", g)
