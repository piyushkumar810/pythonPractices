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
# it will not assign float value