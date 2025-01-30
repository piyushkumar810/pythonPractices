# ------------------------------------ basic aggregating functions in numpy array(lec-08)

import numpy as np
# --------------------------min(x)
# to find mininum value in the given array
var1=np.array([2,4,6,8,15,1])
minValue=np.min(var1)
print(minValue)
print()
var2d=np.array([[3,5,7,9],[6,7,3,155]])
minValue1=np.min(var2d)
print(minValue1)
print("\n")

# --------------------------max(x)
var2=np.array([2,4,6,8,15,1])
maxValue=np.max(var2)
print(maxValue)
print()
var2dM=np.array([[3,5,7,9],[6,7,3,155]])
maxValue1=np.max(var2dM)
print(maxValue1)
print("\n")


# --------------------------argmin(x) --> returns the index place of minimum value
var3=np.array([2,4,6,8,15,1])
Value=np.argmin(var3)
print(Value)
print()

# --------------------------sqrt(x)
var4=np.array([2,4,6,8,15,1])
Value1=np.sqrt(var4)
print(Value1)
print()

# --------------------------sin(x)
var5=np.array([30,45,60,90,180])
Value2=np.sin(var5)
print(Value2)
print()

# --------------------------cos(x)

# --------------------------cumsum(x)
# what is it ?
# eg:- [1,2,3] --> your comulative sum is [1, 1+2=3, 3+3=6]== finally [1,3,6]
var6=np.array([1,4,7,9])
cumsumResult=np.cumsum(var6)
print(cumsumResult)
print()
# like that we have comulative product
cumprodResult1=np.cumprod(var6)
print(cumprodResult1) 
print()

# ---------------------------------------- real use case of comulative product--------------------------
arr1=[100,150,199,200,250,130]
arr2=[10,50,30,40,30,10]

quantity=np.array(arr2)
price=np.array(arr1)

print(quantity, "\n", price)
print()
c=np.cumprod([quantity,price], axis=0)
print(c)
# i need total cost
print("sum = ",c[1].sum())