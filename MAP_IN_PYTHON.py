# --------------------------------map in python
# a map function in python takes a function and a (list, tuple and other itrable object) as an arguument and it returns a new sequence containing the transformed element

# question --> find cube of each element in a list
# eg --> without map
def cube(x):
    return x**3
print(cube(3))

l=[3,6,4,3,7,2]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)

# -------------------using map
def sq(y):
    return y*y
print(sq(5))

l1=[3,5,7,3,2,5]
# newsq=map(sq,l1)
newsq=list(map(sq,l1))
print(newsq)