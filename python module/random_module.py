# --------------------------------python random moodule
# this module can be used to perform random action such as generating random number , printing random value for a list or string

import random

# random()-> return random floating value between 0 to 1
print(random.random())

# randint()-> randint function is used to return random integer value between the given range 
print(random.randint(5,10))

# randrange()-> similar to randint only difference is randerange has three parameter (start, end, step) 
print(random.randrange(5,10,2))

# choice()-> form a given (list, string, tuple..) select random element 
a=["tokyo", "berlin", "india", "china", "russia"]
print(random.choice(a))

string1="piyush"
print(random.choice(string1))

tuple1=(2,4,6,8,1)
print(random.choice(tuple1))

# choices()-> this method used to return multiple random element
mylist=["mango", "banana", "litchi", "ornage", "graps"]
print(random.choices(mylist,weights=[2,1,1,1,2], k=6))