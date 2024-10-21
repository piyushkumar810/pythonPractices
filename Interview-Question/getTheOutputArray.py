# -----------------------------predict the output

from array import *

arr=array('b', [13, 250, -23, -4])
for i in range(4):
    print(arr[i])

# -------------------------output
# OverflowError: signed char is greater than maximum

# we are using signed data of byte type , and it has only capasity to store (+127 to -128) and here you entered 
# 250 which is out of range.