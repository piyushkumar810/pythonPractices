# --------------------- User input in an array

from array import *

arr=array('I', [])

n=int(input("enter the length of array ="))

for i in range(n):
    x=int(input("enter the value ="))
    arr.append(x)

print(arr)

# searching the value given by the user
user=int(input("enter the value you want to search ="))

k=0

for e in arr:
    if(e==user):
        print(f'your desiered value {user} is at {k}th index')
        break
    k=k+1