# how to cut first character and past it to last of the string

string=input("Enter your first name : ")

# Remove the first character and store it
first_char=string[0]

# Create a new string without the first character and add the removed character at the end
new_string=string[1:]+ first_char

print(new_string)

# if you want to encrypt it more then add three character in start and end of the string
prefix="xmg"
suffix="fne"

updated_string=prefix + new_string + suffix
print(updated_string)