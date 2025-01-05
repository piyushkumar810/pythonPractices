# some functions of DataFrame: 

import pandas as pd

dic={"a": [2,4,6,8],
     "b": [1,3,5,7],
     "d": [1,2,3,4],
     1:[5,6,7,8]}

# column attribute - i want to get only "b" column and list 1
# var=pd.DataFrame(dic, columns=["b",1])

# index attribute - you can change index also
# var=pd.DataFrame(dic, columns=["b",1],index=["a", "b", "c", "d"])

# to get paticular value
var=pd.DataFrame(dic)
# to get "a" ka third no row ka data
print(var["a"][3])
print(var)

# -------------------------------------------------------------------------
print("\n")

# creating data framw through lists
l=[[1,2,3,4,5],
   [11,22,33,44,55],
   [111,222,333,444,555]]

var1=pd.DataFrame(l)
print(var1)

# -------------------------------------------------------------------------
print("\n")

# creating data frame through series
dic2={"s": pd.Series([1,2,4,5]),
      "r": pd.Series([3,4,6,7])}

var2=pd.DataFrame(dic2)
print(var2)