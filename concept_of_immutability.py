# in pyhton string are immutable, means cannot be changed after they are created.

a="piyush"
# the string "piyush" is creted and stored in the memory and the variable a refers to this memory.

print(a.upper())
print(a)
# with the help of upper() method a new string with all converted to upper case "PIYUSH" is created.
# but string are immutable, the original string "piyush" remains unchanged in the memory.

# the new string "PIYUSH" is temproraily stored in a seprate memory location for the purpose of printing
# if "PIYUSH" is not assigned to  a variable (b = a.upper()) then it may eventually be garbage collected.

# -------------------------proof where "piyush" is stored
print(id(a))
print(id(a.upper()))
print("\n")

# --------------eg2
# ----------------but what if i will replace the name
b="piyush"
print(b)
print("Address of b (before replace):", id(b))

b=b.replace("piyush","harry")
print(b) # jo previously "piyush" jis address per tha woo tho same address per hai but ab b "harry" ko refer kar rha hai
print("Address of b (after replace):", id(b))


# Step-by-Step Explanation:
# b = "piyush":

# A string "piyush" is created, and the variable b references this string.
# b = b.replace("piyush", "harry"):

# The replace method is called on the string "piyush".
# The method searches for the substring "piyush" in the string b and replaces it with "harry".
# A new string "harry" is created because strings are immutable; the original "piyush" string remains unchanged in memory.
# The variable b is reassigned to reference the new string "harry".
# print(b):

# The current value of b (which is now "harry") is printed.