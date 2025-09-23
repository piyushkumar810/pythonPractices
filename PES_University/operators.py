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