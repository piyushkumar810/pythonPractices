# --------------------------function Argument in python

# 1st default argument
def average(a=9, b=3):
    print("the average of two number is: ", (a+b)/2)

average()

# 2nd keyword argument
def avg(a=9, b=1):
    print("the average is : ", (a+b)/2)
avg(b=9, a=21)

# 3rd required argument
def avg2(a,b=1):
    print("the average is : ", (a+b)/2)
avg(a=21)

# 4th arbitrary argument
def avg3(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is: ", sum/len(numbers))

avg3(5,8,12,35,12,36,78)

# -----------------------------return statement in python

def avg4(*number):
    sum1=0
    for j in number:
        sum1=sum1+j
    return sum1/len(number)

c=avg4(5,8,4,9,7)
print(c)
