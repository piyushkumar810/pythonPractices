# ---------------------------------array functiond in python

from array import *

# buffer_info() -it gives you two information about the array (address, size)
arr=array('i', [3,5,-4,7,8])
print(arr.buffer_info())
print("\n")

# to know which data type is used to store array values
print(arr.typecode)
print("\n")

# to reverse the array list
arr.reverse()
print(arr)
print("\n")

# if you know the length of index
for i in range(5):
    print(arr[i])
print("\n")

# if you dont know the length 
for i1 in range(len(arr)):
    print(arr[i1])
print("\n")

# copying array into another array
newarr=array(arr.typecode, (a*a for a in arr))
for i2 in newarr:
    print(i2)