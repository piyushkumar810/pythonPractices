# ----------------------------------- DataFrame -----------------------------------------
# it is a Two-Dimensional data structure with columns, much likely a tables.

# how it is created?
import pandas as pd

# creating dataframe using list
l=[1,3,5,7,9]
var=pd.DataFrame(l)

print(var)
# hera you can clearly see in the output that here you got both "row and coulmn wise indexed"

# ----------output
'''
   0
0  1
1  3
2  5
3  7
4  9
'''

print("\n")


# creating dataFrame using dictionary
dic={"a": [2,4,6,8],
     "b": [1,3,5,7]}
# remember when you are passing data from dictionary at that time the value of data should be equal.
'''
eg:- 
dic={"a": [2,4,6,8],
     "b": [1,3,5,7,5,4]}

    #  here "a" data is not equal to "b" data so we got an error="value error"
'''

var1=pd.DataFrame(dic)

print(var1)
print(type(var1))