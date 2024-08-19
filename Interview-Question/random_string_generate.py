import random
import string

# Example string
message = input("Enter any string : ")

# Generate three random characters
random_prefix = ''.join(random.choices(string.ascii_letters, k=3))
random_suffix = ''.join(random.choices(string.ascii_letters, k=3))

# Add the random characters to the start and end of the string
new_message = random_prefix + message + random_suffix

print(new_message)