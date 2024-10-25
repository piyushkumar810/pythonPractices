# find the sum of maximum and minimum element from the array

from array import *

# arr=array('I', [23,45,78,3,24])

# n=len(arr)
# if (n==1):
#     print("your sum of min and max value is", arr[0])

# else:
#     if(arr[0]>arr[1]):
#         max=arr[0]
#         min=arr[1]
#     else:
#         min=arr[0]
#         max=arr[1]

#     for i in range(2,n):
#         if(arr[i]>max):
#             max=arr[i]
#         elif(arr[i]<min):
#             min=arr[i]
#     print("your minimum value from the array = ", min)
#     print("your maximum value from the array = ", max)
#     result=min+max
#     print(f"the sum of minimum and maximum value is {result}")




# -------------------------------------or
class solution:
    def findSum(self,arr,n):
        if (n==1):
            return(arr[0])

        if(arr[0]>arr[1]):
            max=arr[0]
            min=arr[1]
        else:
            min=arr[0]
            max=arr[1]
    
        for i in range(2,n):
            if(arr[i]>max):
                max=arr[i]
            elif(arr[i]<min):
                min=arr[i]
        return(max+min)
    
arr=array('I', [23,45,78,3,24])
n=len(arr)
obj=solution()
result=obj.findSum(arr,n)
print(result)