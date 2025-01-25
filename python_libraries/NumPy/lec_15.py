# ---------------------------------- some mor functions of numpy array (lec-15)

import numpy as np
# -------------------- Suffle -->(randomly data will continue changing on each time you run your prpogram)
var1=np.array([2,3,4,5,6])
np.random.shuffle(var1)
print(var1)
print("\n")


# -------------------- Unique--> (you can clearly see all the duplicate values are removed and output is in ascending order)
var2=np.array([2,3,4,5,6,3,4,5,9,7,1,5,5,0,0])
x=np.unique(var2)
print(var2)
print()
print(x)
print()
# ? if you want the index value of the unque value
x_index=np.unique(var2, return_index=True)
print(x_index)
print()
# ? if you want to get count of all elements in the array
x_count=np.unique(var2, return_counts=True) 
print(x_count)
print("\n")


# --------------------------- Resize()--> resize your single dimentional array into 2-d array ,3-d array ..
var3=np.array([2,3,4,5,6,8])
x_2d=np.resize(var3,(2,3))
print(x_2d)
print("\n")


# ----------------------------Flatten()--> it will convert all 2-d, 3-dor multi-d array into singal dimentional array it has 4 order(A,C,F,K)
var4=np.array([2,3,4,5,6,8])
tow_d_array=np.resize(var4,(2,3))
print(tow_d_array)
print()
convert_one_d=tow_d_array.flatten(order="K")
print(convert_one_d)
print("\n")


# --------------------------Ravel()--> same as flatten() with order
