# ------------------------------------- the concept of matrix numpy array in python(lec-17)

import numpy as np

print("-------------- this is matrix--------------")
var=np.matrix([[2,5],[7,8]])
var1=np.matrix([[1,5],[2,3]])
print(var)
print(type(var))
print()
print("1st -> addition and substraction are same in matrix")
add=var+var1
print("ex:- addition = ", add)
print()
print("2nd -> multiplication are different in matrix")
mul=var*var1
print("multiplication = ", mul)
print()
print("functions applied for matrix numpy")
# Transpose = it will convert row data into column data
print("1st : Transpose")
transpose1=np.transpose(var)
print(var)
print(transpose1)
print()

# Swapaxes = is also same as transpose but here we have to give axis
print("2nd : Swapaxes")
swapaxes1=np.swapaxes(var1,1,0)
print(var1)
print(swapaxes1)
print()

# Inverse = functmion used is (np.linalg.inv(matrix_name))
print("3rd : Inverse")
inverse1=np.linalg.inv(var1)
print(var1)
print(inverse1)
print()

# Power = function used is (np.linalg.matrix_power(martix_name, n)) --> where n can be(n=0, n>0, n<0)
var5=np.array([[2,4],[3,7]])
print("4th : Power")
# n=0, we get identity matrix
power1=np.linalg.matrix_power(var5, n=0)
print(var5)
print(power1)
print()
# n<0, you will get  inverse matrix
power2=np.linalg.matrix_power(var5, -2)
print(power2)
print()
# n>0, you will get multiplication matrix
power2=np.linalg.matrix_power(var5, 5)
print(power2)
print()

# Determinate = here functionn used is (np.linalg.det(matrix_name))
detrminant1=np.linalg.det(var5)
print("5th : Determinante")
print(detrminant1)

print()
print("-------------------difference between matrix numpy Vs array numpy--------------------")
print()

print("-------------- this is array--------------")
var3=np.array([[2,5],[7,8]])
var4=np.array([[1,5],[2,3]])
print(var3)
print(type(var3))
print()
print("1st -> addition and substraction are same in array")
add1=var3+var4
print("ex:- addition = ", add1)
print()
print("2nd -> multiplication are different in array")
mul1=var3*var4
print("multiplication = ", mul1)
