# ----------------------------- arithematic operator in python pandas (lec-04)

import pandas as pd

var=pd.DataFrame({"A":[1,2,3,4], "B":[5,6,7,8]})

# adding column "A" and column "B" of dataframe
var["C"]=var["A"]+var["B"]
print(var)
print("\n")

# substraction column "A" and column "B" of dataframe
var["C"]=var["A"]-var["B"]
print(var)
print("\n")

# multiplication column "A" and column "B" of dataframe
var["C"]=var["A"]*var["B"]
print(var)
print("\n")

# division column "A" and column "B" of dataframe
var["C"]=var["A"]/var["B"]
print(var)



print("\n")



# ----------------------------------- performing some logical operations

var1=pd.DataFrame({"A": [10,20,30,40], "B": [50,60,70,80]})

# now i want all the elements of column "A" which is less than 30
var1["less_than_30_in_column_A"]= var1["A"] < 30

# i want all the elements of column "B" which is greater than 60
var1["greater_than_60_in_column_B"]= var1["B"] > 60

print(var1)