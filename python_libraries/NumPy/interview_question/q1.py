# predict the output

import numpy as np
a=np.array([10,20,"30"])

print(a)
print(type(a))
# what is the type of a
# ans--> type of a is array only but the value inside that variable is in string now
# output --> ['10' '20' '30']
print()
# if you want to change the type of array
print(a.astype(float))
print()


# how to find no of elements in this array
b=np.array([[2,3,4,5],[2,5,7,8],[5,1,2,3]])
# lets check with len()
print(len(b))
print()
# size() is the correct function to get no of elements in the array
print(np.size(b))