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
print()

# fibonacci series
def fibonacci(n):
    if n<=0:
        return "input should be positive integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fabio=int(input("enter a number "))
for i in range(1,fabio+1):
    print(fibonacci(i), end=" ")
