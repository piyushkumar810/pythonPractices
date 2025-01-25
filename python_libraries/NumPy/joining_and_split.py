# --------------------- joining and split in NumPy array using(concatenate, stack, array_split) -(lec-13)

# join --> joining means putting content of two and more array into a single array. used--> "concatenate()"

import numpy as np
var1=np.array([1,3,4,5,7])
var2=np.array([3,5,7,9,7])

joinVar=np.concatenate((var1,var2))
print(joinVar)
print("\n")

# joining 2-d array
var3=np.array([[3,5,7],[4,5,6]])
var4=np.array([[8,7,7],[9,6,2]])
print(var3)
print()
print(var4)
print()
new_arr=np.concatenate((var3,var4),axis=1)
print(new_arr)
print("\n")


# stack()--> it is also used to merge two or more array into single array. but here you must give axis.

var5=np.array([1,3,4,5,7])
var6=np.array([3,5,7,9,7])

stackVar=np.stack((var5,var6), axis=0)
# stackVar=np.hstack((var5,var6))  # works along row
# stackVar=np.vstack((var5,var6))  # works along column
# stackVar=np.dstack((var5,var6))  # works along height
print(stackVar)
print("\n")

# split()--> splitting breaks one array into multiple. used-->"array_split()"

var7=np.array([6,8,9,4,5,2])
print(var7)
print()

arr_split=np.array_split(var7, 3)
print(arr_split)
print(type(arr_split))
print(arr_split[1])

# spliting 2-d array
print()
var8=np.array([[6,8],[9,4],[5,2]])
print(var8)
print()
split_2d=np.array_split(var8, 3)
print(split_2d)