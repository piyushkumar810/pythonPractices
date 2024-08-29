# ------------------------------string practice

# ------------rstrip function
str1="!!!!!piyush!!!!!!!!"
print(str1.rstrip("!"))

str2="!!!!!!!!kumar$$$$$$$"
str2=str2.rstrip("$")
# print(str2.rstrip("$"))
print(str2)
print("\n")

# ------------replace function
str3="my name is piyush kumar"
print(str3.replace("kumar", "sinha"))
print("\n")

# ------------split and join function
str4=str3.split(" ")
print(str4)
print(type(str4))
str5=' '.join(str4)
print(str5)
print(type(str5))
print("\n")

# Q) question is, is == work wiith string
str6="piyush"
str7="piyush"
print(str6 == str7)