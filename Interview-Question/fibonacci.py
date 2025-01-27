# write a program to get fibonacci series up to 10 number

def fibonacci_series(a,b):

    n=int(input("enter the number "))
    print(a)
    print(b)
    i=1
    while(i<=(n-2)):
        c=a+b
        a=b
        b=c
        print(c)
        i+=1

fibonacci_series(0,1)