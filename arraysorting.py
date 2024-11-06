# ------------------------------sorting of an array

from array import *

arr=array('I', [5,9,2,4,18,20,14])
sorted_arr=sorted(arr)
print(sorted_arr)

# for ascending order
sorted_arr_ascending=sorted(arr, reverse=True)
print(sorted_arr_ascending)
