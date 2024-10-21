# ------------------------------how to use while loop in an array

from array import *

arr= array('I', [45,67,32,23,38])

newarr=array(arr.typecode, (a+a for a in arr))

i=0
while(i<len(newarr)):
    print(newarr[i])
    i=i+1