# -----------------------------------recursion in python

# eg 1) factorial number

def factorial(n,f=1):
    if(n!=0):
        f=f*n
        factorial(n-1,f)
    else:
        print("a factorial value = ", f)
    
a=int(input("enter any value "))
factorial(a)

print("\n")

# eg 2) sum of series 1+3+5+7+......+n term

def series(n,s):
    for i in range(1,n+1):
        # print(i)
        s=s+(2*i-1)
    print(s)

series(5,0)

# but using recursion
def sumSeries(i,n,s):
    if(i<=n):
        s=s+(2*i-1)
        sumSeries(i+1,n,s)
    else:
        print("sum of series = ", s)

b=int(input("enter any number "))
sumSeries(1,b,0)
print("\n")

# printing fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print the Fibonacci series up to the n-th term
n = int(input("Enter the number of terms: "))
for i in range(1, n+1):
    print(fibonacci(i), end=" ")
