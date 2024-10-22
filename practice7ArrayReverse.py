from array import array

arr = array("I", [2, 5, 8, 4, 7])
# Creating an array

# # Print the original array
# print("Original array:", arr)

# # Reverse the array in place
# arr.reverse()

# # Print the reversed array
# print("Reversed array:", arr)

# -----------------reversing array without using function

n=len(arr)
for i in range (n//2):
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp
print(arr)