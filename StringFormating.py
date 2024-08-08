# ----------------------------------------------String Formating

# before formatting was done with formate () method
letter="hey my name is {0} and i am from {1}"
country="india"
name="piyush"

print(letter.format(name,country))

# now formatting was done f-string
name1="piyush"
country1="india"
print(f"hey my name is {name1} and i am from {country1}")

# eg 2
price=49.09999
txt=f"for only {price :.2f} doller !"
print(txt)

# eg3
print(f"{2*30}")
print(type(f"{2*30}"))

