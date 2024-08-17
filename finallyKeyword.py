# -----------------------------------------finally kekyword in python

# eg 1
try:
    l=[4,7,9,5]
    i=int(input("Enter the index : "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("i am always executed")

print("\n")

# ----------------here one question arrises
# what is the difference between above program and this program
try:
    a=[4,7,9,5]
    n=int(input("Enter the index : "))
    print(a[n])
except:
    print("some error occured")
print("i am non-finally block but i will executed")
# here also we can use functionality of finally keyword without using finally keyword

print("\n")
# -------------------------------------------solution
# we can see the difference of both program when we write this program inside one function

def fun1():
    try:
        b=[4,7,9,5]
        m=int(input("Enter the index : "))
        print(b[m])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed")
    print("i am always executed")

x=fun1()
print(x)