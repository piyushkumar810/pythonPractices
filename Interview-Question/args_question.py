# will the program run  or not 

#---------------- q1
def add(*args, name):
    c=0
    print(name)
    for i in args:
        c+=i
    print(f"sum is {c}")

# add(1,2)
# add(2,4,7,"piyush")
# the above both parameter passedfunction will raise an error because these all argument is taken in args only

add(2,5,7, name="piyush")
# this will work because name="piyush" is different type of argument whoch is not accepted by *args

#----------------- q2

# def my_function(**kwargs, *args):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# my_function(1, 2, name="Alice", age=30)

# this program will raise an error because order should be maintained (*args, **kwargs)