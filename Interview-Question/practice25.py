# factorial of a number

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        res=n*fact(n-1)
        return res

num=int(input("enter a number "))
factorial=fact(num)
print(factorial)