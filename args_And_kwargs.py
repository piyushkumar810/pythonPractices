# -------------------------------   *args and **kwargs in python

# --------- *args
# it allow you to pass variable number  of non keyword argument to a function
#  it takes all the argument  in tuple form(tuple is immutable) 
# eg
def my_fun(*args):
    c=0
    for i in args:
        c+=i
    print(f"sum is {c}")


my_fun(1,2)
my_fun(1,5,78,4)
my_fun(4,6,8,3,56,7,4,4)
print("\n")

# ----------- **kwargs
#  it allow you to pass variable number  of keyword argument to a function
# it stores all the argument in the form of dictionary
# eg
def my_fun1(**kwargs):
    for key,value in kwargs.items():
        print(f" {key } = { value}")

my_fun1(name="piyush" , age=22, state="jharkhand")