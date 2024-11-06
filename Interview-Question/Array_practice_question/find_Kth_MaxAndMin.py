# ---------------------------find kth max and min element in array

from array import *

class solution:
    def kthSmallest(self, arr, k, l):
         newarr=sorted(arr)
         print(newarr)

         for i in range(l-1):
              if(i==(k-1)):
                   print(newarr[i])

sol=solution()
arr=array('I', [7,3,4,6,25,20])
l=len(arr)
# print(l)

k=int(input("enter the value and the value should be less than the size of the array : "))

sol.kthSmallest(arr,k,l)