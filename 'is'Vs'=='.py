# ---------------'is' vs '==' in python

# "is" --> is compares the exact location of object in memory
# "==" --> operator compare the value of an object

#--------------- eg1 
a1=4
b1="4"

print(a1 is b1)
print(a1 == b1)
print("\n")

#---------------- eg2
a2=[2,4,6]
b2=[2,4,6]

print(a2 is b2)
print(a2 == b2)
print("\n")

# -----------------eg3
a3=4
b3=4

print(a3 is b3)
print(a3 == b3)
print("\n")

# -----------------eg4
a4=(1,2)
b4=(1,2)

print(a4 is b4)
print(a4 == b4)
print("\n") 

# ------------------eg5
a5=None
b5=None

print(a5 is b5)
print(a5 is None)
print(a5 == b5)