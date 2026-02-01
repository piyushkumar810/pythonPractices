def sum_of_digits(num):
    s=0
    while(num>0):
        rem=num%10
        num=num//10
        s=s+rem
    return s

print(sum_of_digits(5))
print(sum_of_digits(15))
