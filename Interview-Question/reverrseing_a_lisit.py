# ------------------------------------ reversing a list

# Using slicing:
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]


# Using reverse() method (in-place reversal):
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]


# Using reversed() function (returns an iterator):
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]


# Using a for loop:
def reverse_list(arr):
    n = len(arr)
    reversed_arr = [0] * n  # Creating an empty list of the same size
    for i in range(n):
        reversed_arr[i] = arr[n - 1 - i]
    return reversed_arr

arr = [1, 2, 3, 4, 5]
print(reverse_list(arr))  # Output: [5, 4, 3, 2, 1]


# Using two-pointer approach (in-place reversal):
def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

arr = [1, 2, 3, 4, 5]
reverse_in_place(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]