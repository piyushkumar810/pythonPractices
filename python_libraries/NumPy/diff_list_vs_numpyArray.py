# -----------------------Difference between NumPy array and list in python: (lec-02)
'''
	Data type storage-> list can store multiply datatype.
                     ->numpy array can work with single datatype at a time.

	Importing module ->list is in-built datatype (you don’t have to import it.)
                     -> but in numpy array (you need to import package in python to work with array)

	Numerical operation ->in list we can work with numerical op but slow.
                         ->in numpy array it work very fast.
 
	Modification capability ->list has more modification capability than numpy.
                            ->numpy array has less modification capability.

	Consumes less memory ->list consumes more memory than numpy array.
                          ->numpy array consumes less memory.

	Fast as compared to python list  ->numpy array is fast as compared to python.

	Convenient to use
'''

# Note:-
#  if you want to check array runs fast or list use function -> “%time it”  (this will work for single line code).
# but if you want to check ki pura program ke execution hone mai kitne tike lag rha hai then use->” %%time it”


import numpy as np

# print(%timeit [4 for j in range(1, 9)])
# this function will work in jupiter notebook

import time as t

# start_time = t.time()

# # Your code to measure time
# [4 for j in range(1, 9)]

# end_time = t.time()
# execution_time = end_time - start_time
# print(f"Execution Time: {execution_time} seconds")

## ------------------ and time for array

start_time = t.time()

# Your code to measure time
arr = np.arange(1, 9)**2

end_time = t.time()

# Calculate the execution time in seconds
execution_time_seconds = end_time - start_time

# Convert to microseconds
execution_time_microseconds = execution_time_seconds * 1_000_000

print(f"Execution time of array is {execution_time_microseconds} microseconds")