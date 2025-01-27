# to check the number is prime or not

def is_prime(n):
    for i in range(2,int(n/2)):
        if(n%i==0):
            return f"the no {n} is not prime "
        else:
            return f'the no {n} is prime '


n=int(input("enter the number of which you want to check the prime = "))
result=is_prime(n)
print(result)