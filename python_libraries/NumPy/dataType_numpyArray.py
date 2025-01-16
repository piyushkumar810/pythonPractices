# ---------------------------------- data type in numpy array(lec-06)

import numpy as np

var1=np.array([1,2,3,4,5,6])
print(var1)
print(var1.dtype)
print()

var2=np.array([1,8.2,99.3,4,98.5,6])
print(var2)
print(var2.dtype)
print()

var3=np.array(["piyush","khusham","sohal"])
print(var3)
print(var3.dtype)
print()


# changing data type
var4=np.array([1,2,3,4,5,6], dtype="int64")
print(var4)
print(var4.dtype)
print()

var5=np.array([1,2,3,4,5,6], dtype="f")
print(var5)
print(var5.dtype)
print()