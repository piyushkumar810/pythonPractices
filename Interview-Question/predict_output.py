import sys

i = 10
j = 10
k = 4

# Equivalent of sizeof(k /= i + j) in Python
size = sys.getsizeof(k / (i + j))  # k /= (i + j) will be evaluated here
print(size)

# Print the value of k after the division
k /= (i + j)  # k = k / (i + j)
print(k)

# --------------------------------------explanation----------------------------------------
# Step-by-Step Execution
# Initial Values:

# i = 10, j = 10, k = 4.
# sys.getsizeof(k / (i + j)):

# Python evaluates k / (i + j):
# i + j = 10 + 10 = 20.
# k / (i + j) = 4 / 20 = 0.2 (Python uses floating-point division).
# The result (0.2) is a floating-point number (float type).
# sys.getsizeof(0.2) typically returns 24 bytes for a float object (this can vary depending on the Python implementation and system).
# Value of k After Division:

# k /= (i + j) updates k:
# k = 4 / 20 = 0.2.
# k becomes a float with the value 0.2.
# Output:

# First print(size) outputs the size of the floating-point result (24 bytes, typically).
# Second print(k) outputs the value of k (0.2).