# ----------------------------generator in pyhton

# A generator in Python is a way to create values one at a time, instead of all at once.

# --------or

# A generator in Python is a special type of iterator that is used to generate a sequence 
# of values lazily, meaning it produces items one at a time and only as needed, rather than 
# computing and storing them all at once. This is particularly useful for handling large 
# datasets or streams of data efficiently.

# it uses yield keyword

def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Pauses the function and returns the current value
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)