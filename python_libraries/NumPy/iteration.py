# ------------------------------- iteration of numpy array (lec-11)

# iteration in single dimention array
import numpy as np

var1=np.array([22,4,5,6,77,7,5])
print(var1)
print()
for i in var1:
    print(i)
print("\n")

# iterating 2d array
var2=np.array([[1,4,7,9],[9,6,4,3]])
print(var2)
print()
for j in var2:
    print(j)
#  but using this you cannot iterate each value to iterate each value for 2d array you have to use double for loop
'''
------------output
[1 4 7 9]
[9 6 4 3]
'''

print()
for k in var2:
    for l in k:
        print(l)
'''
----------------output
1
4
7
9
9
6
4
3
'''

print("\n")
# here comes the function "nditer()" so that you can easily iterate multideentional  array
var3=np.array([[[1,4,7,9],[9,6,4,3]]])
print(var3)
print()
for a in var3:
    for b in a:
        for c in b:
            print(c)

print('\n')
# using nditer()
for d in np.nditer(var3):
    print(d)