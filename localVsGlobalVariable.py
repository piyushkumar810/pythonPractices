# ---------------------------local and global variable in python

# ------------------drefferentating local and global variable
x=6
print("this is global variable", x)

def myfun():
    y=7
    x=3
    print("this x is in local variable ", x)
    print("this is local variable ", y)

myfun()
print("the variable x inside the function will not override global variable x ", x)
# print("y is inside the function so it is local variable so, you cannot access outside the scope of local variable",y)

print("\n")
# ----------------------------but you can make local variable as global by using "global" keyword
# eg

a=20
print(a)

def gobal():
    global a
    print(a)

gobal()
print(a)