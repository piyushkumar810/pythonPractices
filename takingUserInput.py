# in python user input is taken by "input()" function.
# eg 1
a=input()
print("my name is :", a)
print("\n ")

# eg 2
b=input("Enter your name: ")
print("my name is :", b)
print("\n")

# eg 3
# python bydefault consider user input as an String
x=input("Enter 1st number :")
y=input("Enter 2nd number :")
print(x+y) 

# to correct this we have to explicitly typecast it
print(int(x)+int(y))
