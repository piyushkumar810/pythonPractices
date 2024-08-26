# ----------------------reduse in pyhton
# the reduce function is applies a function to a sequence and retuerns a single value

# eg
from functools import reduce
list1=[4,6,8,3,5,8,3]
 
# def sum(x,y):
#     return x+y

# newlist=reduce(sum,list1)
# print(newlist)

# ------------or by lambda function
newlist=reduce(lambda x,y: x+y, list1)
print(newlist)