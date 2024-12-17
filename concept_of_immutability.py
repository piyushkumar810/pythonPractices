# in pyhton string are immutable, means cannot be changed after they are created.

a="piyush"
# the string "piyush" is creted and stored in the memory and the variable a refers to this memory.

print(a.upper())
# with the help of upper() method a new string with all converted to upper case "PIYUSH" is created.
# but string are immutable, the original string "piyush" remains unchanged in the memory.

# the new string "PIYUSH" is temproraily stored in a seprate memory location for the purpose of printing
# if "PIYUSH" is not assigned to  a variable (b = a.upper()) then it may eventually be garbage collected.

# -------------------------proof where "piyush" is stored
print(id(a))
print(id(a.upper()))