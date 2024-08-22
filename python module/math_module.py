# ------------------------------------math module in python

import math as mt

print(type(mt))
a=int(input("enter a value : "))

# .ceil()--> round a number upward to its nearest integer
print(mt.ceil(a))
print(mt.ceil(2.43))
print(mt.ceil(-1.32))
print("\n")

# .exp()--> returns E raised to the power x(E^x)
print(mt.exp(a))
print(mt.exp(-2.43))
print("\n")

# .fabs()--> method returns absolute value number as float and always return in positive value
print(mt.fabs(-23.546))
print(mt.fabs(43))
print("\n")

# .factorial()--> returns factorial of a number 
print(mt.factorial(5))
print(mt.factorial(8))
print("\n")

# .floor()--> round the number down to nerest integer
print(mt.floor(2.43))
print(mt.floor(-4.34))
print("\n")

# .pow()--> returns the value of x raised to the power y.
print(mt.pow(3,4))
print(mt.pow(-4,3))
print("\n")

# .comb()--> returns the number of wasy picking k unordered outcoome from n possiblities, without repetation, also known as combination
print("this is combination")
n=int(input("enter the number of item choose from : "))
k=int(input("enter the number of possiblities to choose : "))
print("the combination is = ", mt.comb(n,k))
print("\n")

# .gcd()--> returns greatest common divisor
print(mt.gcd(3,6))
print(mt.gcd(43,56,34))
print("\n")

# .trunc()--> returns only integer part of the number and removes all deciaml part
print(mt.trunc(2.456789))
print(mt.trunc(-245.65456))