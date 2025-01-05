# using array creating a series data

import pandas as pd

dictionary_data={"name" : ["python", "c", "c++", "java"], 
                 "popularity" : [12,13,14,15],
                 "rank" : [1,4,3,2]}

var=pd.Series(dictionary_data)
print(var)
# here data type is object why? because here we are using mixed data type 

print("\n")

# making series with single data
s=pd.Series(12)
print(s)

print("\n")
# now i want ki single data k multiple blocks ban jay
m_b=pd.Series(12, index=[1,2,3,4,5,6,7])
print(m_b)