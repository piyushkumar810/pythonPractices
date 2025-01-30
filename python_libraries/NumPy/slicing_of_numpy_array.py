import numpy as np

# slicing of one-dimentional array
a=np.array([2,34,56,78,90])
print(a[0:4])
print()
print(a[0:5])
print()
print(a[:])
print()
print(a[0:])
print()
print(a[:5])
print()
print(a[::-1])
print()
print(a[-4:-1])
print("\n")

# slicing if two-dimentional array
aa=np.array([[4,5,6,7,8],[40,50,60,70,80]])

print(aa[0:2,0:2])
# first 0:2 is for 1st row and 2nd 0:2 for the 2nd row
print()

# we can not do like this
# print(aa[0:2,0:3])
# both value should be equal

# if i want 5 and 6 from 1st row then
print(aa[0,1:3])
print()
print(aa[1,1:3])
print()