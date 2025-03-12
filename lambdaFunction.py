# --------------------------------knowing lambda function
# lambda function is an annomyous function (means a function without name) .it does not contain return statement

# eg--> without using lambda function
def sum(x,y):
    return x+y
a=sum(10,30)
print(a)

# eg --> using lambda function
a1=lambda x1,y1:x1+y1
print(a1(20,30))

# eg3 -->passing function as an argument
def cube(c):
    return c*c*c
print(cube(5))

def appl(fx, value):
    return 6+fx(value)

print(appl(cube,2))
# ------------or
# print(appl(lambda x:x*x*x ,2))