# ----------------------------filter in pyhton
# filter function filters a given sequence of element based on given condition and returns a new sequence

# eg
def filter_function(x):
    return x>4

list1=[4,6,8,2,9,5,3,0]
newlist=list(filter(filter_function,list1))
print(newlist)


# using lambda function in filter function
list2=[4,2,6,7,8,3,2,7]
newlist1=list(filter(lambda x:(x>4), list2))
print(newlist1)