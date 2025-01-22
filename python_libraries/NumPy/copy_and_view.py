# -------------------------------- copy vs view in numpy array

import numpy as np

# ---------------------- copy()
var=np.array([1,2,3,5])
copy=var.copy()
print("var ", var)
print()
print("copy ", copy)
print("\n")

# ------------------------ view()
var1=np.array([1,2,3,5])
copy1=var1.view()
print("var1 ", var1)
print()
print("copy1 ", copy1)
print("\n")

# if both functions are same then what is the basic difference?
'''
copy()--> Creates a new array: When you use the copy function, it creates a completely new and independent array.

          Independent memory: Changes made to the copied array do not affect the original array, and vice versa.

view()--> Creates a view (shallow copy): The view function creates a new array object that refers to the same data as the original array.

          Shared memory: Changes made to the view affect the original array, as both reference the same memory.
'''


# example of copy()
print("----------------- copy() ---------------")
original = np.array([1, 2, 3])
copied = original.copy()

copied[0] = 99
print("Original array:", original)  # [1, 2, 3]
print("Copied array:", copied)     # [99, 2, 3]
print()



# example of view()
print("------------------- view()-----------------")
original1 = np.array([1, 2, 3])
viewed1 = original1.view()

viewed1[0] = 99
print("Original array:", original1)  # [99, 2, 3]
print("Viewed array:", viewed1)      # [99, 2, 3]