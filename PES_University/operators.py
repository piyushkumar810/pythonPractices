# ---------------------------arithematic operator
a=10
b=20
print(f"{a+b}")

print(10+20)
print(b-a)
print(a*b)
print(9 ** 0.5)  #
print(10//3)   #since 10/3= 3.3333  -> but floor =3
print(-7//2)  #-4(since -7/2 =-3.5 -> floor= -4)

# -----------------------------assignment operator
x=10

x+=5
print(x)

x*=2
print(x)
# ----or
# print(x*=2)   # you cannot pass expression into a statement

x-=5
print(x)


# -------------------------------- bitwise operator
# AND (&)
bitwiseAnd=6 & 3
print(bitwiseAnd)

# OR
bitwiseOr=6 | 3
print(bitwiseOr)

# XOR
bitwiseXor=6^3
print(bitwiseXor)

# leftshift
bitwiseLeftShift=5
print(bitwiseLeftShift)

# ----------------------------------comparision operator
# <  ->
# >
# ==
# !=
# >=
# <=


# --------------------------------- identity operator
# is and is not are the identity operator in python

print()
a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)

# ----------------------------------- membership operator (in and not in)
print()
x=[1,2,3,4,5]
print(3 in x)
print(7 in x)

name="python"
print("p" not in name)
print("z" not in name)


# ---------------------------------- data type in pyhton
print()
# there are two type of conversion
# 1. implicit type conversion
x1=10
y1=2.5

result=x1+y1
print(result)  #12.5
print(type(result)) #<class 'float'>

# int to string
y2=25
print(str(y2))
print(type(str(y2)))

# string to a float
z1="3.14"
print(float(z1))

# ------------------------question 1 (predict the output)
n11="one"
n22=23

print(type(n11))         #string
# explicut type casting
# n11=int(n11)              cannot convert
# print(type(n11))

# sum1=n11+n22    #can only concatenate str (not "int") to str
# print(sum)
# print(type(sum))

# ----------------------------- Python indentation
print()
number = 5

if number > 0:
    print("Number is positive")
    for i in range(number):
        print(f"Counting: {i+1}")
print("This line is outside the if block")

# ------------------------ working wiith input() function
print()
x4=input("enter the value you want")
print(x4)
print(type(x4))

# --------------------- formatted output
print(f"section : %c, temp : %5.2f %{(1,05.333)}")

# string formatting using format()
print()
name1="harry"
age=22
print("Name : {}, Age: {}".format(name1,age))

# positional formatting
print("First: {0}, Second: {1}, Again First: {0}".format("A","B"))

# keyword formatting
print("Name: {n}, Age:{a}".format(n="harry", a=22))

# advanced fprmatting
pi = 3.14159
print("pi : {:.2f}".format(pi))  
# print("Number: {:.5d}".format(42))  # Corrected spelling of "Number"
print("Left align: {:.<5d}".format(42))  # Correct: Left-aligns with dots

# ------------------------------------------ headers and Blocks
# header--> header is a keyword flowed by 
# A clauses= header + suits