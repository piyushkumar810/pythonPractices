# ------------------------------- Broadcasting in NumPy array (lec-10)

# what is broadcasting in numpy array?
import numpy as np

# var1=np.array([4,5,6,7])
# var2=np.array([5,6,8])

# print(var1 + var2)
print("\n")

'''
-------------------output
ValueError: operands could not be broadcast together with shapes (4,) (3,)
'''
# --------------------------------why this broadcast error
# rules to do operation in array

# 1--> Same Dimension 
var1=np.array([4,5,6,7])
var2=np.array([5,6,8,7])
print(var1 + var2)

# 2--> if dimension are not same 
var3=np.array([4,5,6])
print(var3.shape)
print()
print(var3.ndim)
print()
print(var3)
print("\n")

var4=np.array([[5],[6],[8]])
print(var4.shape)
print()
print(var4.ndim)
print()
print(var4)
print("\n")

# is this addition possible
# yes (1*3) (3*1)=will give (3*3) matrix
print(var3 + var4)

print("\n")
# can you add the array of (2*1) and (2*3)
# yes the resultant matrix is of (2*3)