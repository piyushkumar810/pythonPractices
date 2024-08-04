# -------------------------function in python

# eg1)
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

calculateGmean(a=20,b=30)
calculateGmean(30,6)

# eg2)
def name(fname,lname):
    print("hellow", fname, lname)
name("piyush", "kumar")

# eg3) factorial
def factorial(a):
    f=1
    while(a>0):
        f=f*a
        a=a-1
    print(f)

factorial(4)
# factorial(a=input("enter any value: "))
factorial(6)
