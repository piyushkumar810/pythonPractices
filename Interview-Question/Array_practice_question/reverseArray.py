# ----------------------------reverse an array
from array import *

arr=array('I', [2,5,7,6,9])

a=len(arr)
for i in range (a//2):
    tem=arr[i]
    arr[i]=arr[a-i-1]
    arr[a-i-1]=tem
print(arr)