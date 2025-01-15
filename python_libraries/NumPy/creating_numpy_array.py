# ------------------- creating NumPy array (lec-03)

# to create numpy array you can use "np.array()"

import numpy as np
a=np.array([1,2,5,67])
print(a)
print(type(a)) # this is of array type
print("\n")

# # you want the user to give value
# l=[]
# for i in range(1,5):
#     get_data=int(input("enter the value : "))
#     l.append(get_data)

# # this is of list type
# print(l)
# print(type(l))
# # now this is of array type
# print(np.array(l))
# print(type(np.array(l)))
# print("\n")


# -----------------------how to identify the dimension of array --> array_name.ndim
# 1-D array
b=np.array([1,2,5,67])
print(b)
print(type(b))
print(b.ndim)
print("\n")

# 2-D array
c=np.array([[1,2,4,5],[3,4,5,6]])
print(c)
print(c.ndim)
print("\n")

# 3-D array
d=np.array([[[32,4,5],[34,5,6],[3,45,6]]])
print(d)
print(d.ndim)
print("\n")

# creating multidimention array
e=np.array([2],ndmin=10)
print(e)
print(e.ndim)