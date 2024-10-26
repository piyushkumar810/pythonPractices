# ----------------------------------------practice arrray program

from array import *

arr=array('I', [2,7,11,15])

userInput=int(input("enter the target value"))
n=len(arr)
i=0
while(i<n):
    for j in range(1,n):
        result=arr[i]+arr[j]
        if(userInput==result):
            print(i , "and" , j)
        break
    i=i+1