# --------------------------- insert and delet array function in numpy array(lec-16)

import numpy as np
# --------------------------insert(arr_name, positiion, value)
var1=np.array([3,5,7,91,1])
print(var1)
print()
# inserting single value
insertion1=np.insert(var1,3,8)
print("inserting single value",insertion1)
print()
# inserting one array
insertion2=np.insert(var1,3,[8,9,10])
print("inserting single value",insertion2)
print()
# inserting single value at multiple places
insertion3=np.insert(var1,(2,4,5), 40)
print("inserting single value",insertion3)
print()
# inserting float value
# it will not assign float value because the dataType of the array is int32
insertion4=np.insert(var1,4,6.5)
print("insert float value",insertion4)
print()

# inserting in 2-d array
var2=np.array([[2,4,6],[3,5,7]])
# inserting along row
insertion5=np.insert(var2,2,6,axis=0)
print(insertion5)
print()

# inserting along column
insertion6=np.insert(var2,2,6,axis=1)
print(insertion6)
print()

# using append function to insert the value?
insertion7=np.append(var1,6.5)
print(insertion7)
print()
# inserting multiple value using append function
insertion8=np.append(var1,[23,45,67,99])
print(insertion8)
print()
# inserting values in 2-d array usingn append function
insertion9=np.append(var2, [[45,78,89]], axis=0)
print(insertion9)
print("\n")


# ---------------------------------- deletion
var3=np.array([37,59,7,91,100])
print(var3)
print()
delet1=np.delete(var3,1)
print(delet1)

delet2=np.delete(var3,(0,3))
print(delet2)