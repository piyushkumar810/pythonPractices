# ---------------------------------------accessing characters in string

name="piyush kumar"
# in python index place starts from 0 and goes to (n-1)
print(name[0])
print(name[5])
print(name[10])

print(name[-2])
# negative index works like (total length of name=>12-2 = 10 so, finally it will be print(name[10])  )
print(name[-5])

# but we will not access characters manually 
# we use the concept of looping

for character in name:
    print(character)
