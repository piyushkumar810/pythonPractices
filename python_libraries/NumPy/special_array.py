# ------------------------ special NumPy array (lec-04)

import numpy as np

#--------------------  array filled with 0's
arr_zeros=np.zeros(4)
print(np.array(arr_zeros))
print("\n")
# you can create two dimention array also
arr1_zeros=np.zeros((3,4))
print(np.array(arr1_zeros))
print("\n")


#----------------------- array filled with 1's
arr_one=np.ones(4)
print(np.array(arr_one))
print("\n")
# you can create two dimention array also
arr1_one=np.ones((3,4))
print(np.array(arr1_one))
print("\n")


# ---------------------  create an empty array
arr_empty=np.empty(4)
print(np.array(arr_empty))
print("\n")
# you can create two dimention array also
arr1_empty=np.empty((3,4))
print(np.array(arr1_empty))
print("\n")
# here you output is 
'''
[1. 1. 1. 1.]

[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]] this is because jo previously data ratha hai wo automatically fill ho jata ahi empty array mai
'''


#------------------------  an array with range of element
arr_range=np.arange(4)
print(np.array(arr_range))
print()


# ------------------------ array diagonal element filled with 1's
arr_dignol=np.eye(3)
print(arr_dignol)
# for multidimentional array
print()
# pass square matrix only
arr1_diagnol=np.eye(5,7)
print(arr1_diagnol)
print()


# ------------------------- create an array with values that are spaced linearly in a specified interval.
arr_linspc=np.linspace(0,10, num=5)
print(arr_linspc)
print()
arr1_linspc=np.linspace(0,20, num=5)
print(arr1_linspc)