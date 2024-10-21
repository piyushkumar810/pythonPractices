# ------------------------------Array in python

# an array is a collection of homogeneous or similar data type.

# in python you cannot use array directly because array function are kept in  a module. and when we mant 
# to use array we have to import it.  eg:- import array, import array as arr, from array import *

# eg:- 

from array import *

arr=array('b', [13, 20, -34, -27, 5])
for x  in arr:
    print(x)

print("\n")


# if you want to print the value through their indexes then:

arr1=array('B', [3,45,78,234,34])

for x1 in range(len(arr1)):
    print("the index value is ",  x1 ,"and value is ", arr1[x1])