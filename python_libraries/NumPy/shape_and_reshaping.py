# ------------------- shape and reshaping in numpy array (lec-09)

import numpy as np
# --------------------------------shape in numpy
# it will tell you m*n (means size of array)

var1=np.array([[1,4,7],[2,5,8]])
print(var1)
print()
print(var1.shape)
print()

# creating multi-dimentional array
var2=np.array([1,4,7,9], ndmin=4)
print(var2)
print()
print(var2.ndim)
print(var2.shape)
print()

# -------------------------------- reshape the array in numpy
# here we will see how we will convert multi-dimentional array into one dimentional array  and one dimentional to mlti-dimentional

var3=np.array([1,2,3,4,5,6,7,8,9])
print(var3)
print(var3.ndim)
print()
reshapeVar3=var3.reshape(3,3)
print(reshapeVar3)
print(reshapeVar3.ndim)
print()

# creating 3 dimentional array
var4=np.array([1,2,3,4,5,6,7,8,9,0,11,12])
print(var4)
print(var4.ndim)
print()

resahpe2=var4.reshape(3,2,2)
print(resahpe2)
print(resahpe2.ndim)
print(resahpe2.shape)
print()

convertIntoOneDim=resahpe2.reshape(-1)
print(convertIntoOneDim)
print(convertIntoOneDim.ndim)