# ------------------------------explicit type casting
print("explicite type conversion converts one data type to another data type \naccording to developer or programmer")

# eg 1
a="8"
b="5"
c=int(a)+int(b)
print(c)
print(type(c))

# eg 2
string="15"
number=7
string_number=int(string)
sum=number+string_number
print("the sum of both the number is =", sum)

#------------------------------- implicite type casting
print("converts one data type to another datatype automatically by pyhton when their \nis required ")

# eg
a1=1.9
a2=8
sum1=a1+a2
print(sum1)
print(type(sum1))