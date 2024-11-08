# given an array which consists of only 0,1 and 2. sort an array without using any sorting algorithm or any 
# built-in functions

# remember the time complexity must be O(N)

from array import *

class solution:
    def sortArray(self, arr, n):
        cnt0=0
        cnt1=0
        cnt2=0

        for i in range(n):
            if arr[i]==0:
                cnt0 +=1
            elif arr[i]==1:
                cnt1 +=1
            elif arr[i]==2:
                cnt2 +=1

        i=0
        while(cnt0 > 0):
            arr[i]=0
            i +=1
            cnt0 -=1
        
        while(cnt1 > 0):
            arr[i]=1
            i +=1
            cnt1 -=1
        
        while(cnt2 > 0):
            arr[i]=2
            i +=1
            cnt2 -=1

        return arr

sol=solution()
arr=array('I', [])
n=int(input("Enter the size of array : "))

for i in range(n):
    x=int(input("Enter the value : "))
    arr.append(x)

print(n)
print(arr)

print(sol.sortArray(arr,n))