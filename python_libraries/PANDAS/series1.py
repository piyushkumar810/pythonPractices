# -------------------------------------Series
''' it is defined as One-Demesional array that is capable of storing various data types.'''

import pandas as pd

# here you can take any type of data like : list, array, dictonary ..
# here we are taking list data type
x=[54,67,45,84,70]
var=pd.Series(x, index=["Dsa", "C", "C++", "python", "java"], dtype=float, name="Subjects")
# with the help of Series method only you got the data in well mannered(like excel sheet data) way with proper(by-default index)

print(var)
'''
--------------------- output
0    54
1    67
2    45
3    84
4    70
dtype: int64

'''
# how to check is this series belongs to  pandas librery or not - using type function
print(type(var)) 
'''
--------------------- output
<class 'pandas.core.series.Series'>
'''

# ----------  this series method consist of many functionality(look at the above example)
# like:- 
# 1st -> you want to change the index name(by-default 0,1,2...) -->"index=[give your on indexes]" (look above example)
# 2nd -> you can also change the data type (by-default = int64) --> "dtype= which data type you want"
# 3rd -> you can give the name of the data --> "name= "any name which is suitable to your data" 