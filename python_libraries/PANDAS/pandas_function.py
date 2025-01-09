# ------------------------------------ pandas function (lec-08)

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv")

# 1st keyword - want to get how many records in the csv files (means total index).
# --------------use "index" keyword
print(csv_1.index)
print("\n")

# 2nd keyword - you want all the columns in that record
# ------------- use "columns" keyword
print(csv_1.columns)
print("\n")

# 3rd method - if want to get (min value ,max value or value greater than 50% --means details of your record)
# -------------- use "describe" method --> only numerical value will be calculated
print(csv_1.describe())

'''
-----ouutput------
        std_roll   std_mark
count   5.000000    5.00000
mean   33.000000  366.00000
std    15.033296   52.84411
min    10.000000  280.00000
25%    28.000000  350.00000
50%    35.000000  395.00000
75%    44.000000  400.00000
max    48.000000  405.00000
'''
print("\n")


# 4th - if you to get limited amount of data for lots of data
# --------- use "head(no of dara)" function -> this will show data form top
# --------- use "tail(no of dara)" function -> this will show data form bottom
print(csv_1.head(2))
print(csv_1.tail(2))
# or with slicing you can get middle data
print(csv_1[1:4])
print(csv_1[ :3])
print(csv_1[2:])
print(csv_1[:])
print("\n")

# currently the data type of this excel file is data frame but you want to change index data type 
print(type(csv_1))
print(csv_1.index.array)
print("\n")

# you can convert all data into array
print(csv_1.to_numpy)
print("\n")

# if you want your data in descending order:
# axis=0 (arranging using index)
# axis=1  (means arranging through columns)
print(csv_1.sort_index(axis=0,ascending=False))
print('\n')

# if you want to cahnge the value of any index
# ----------use "loc" method
csv_1.loc[0,"std_name"]="saurav"
print(csv_1)

# one more use of loc method -> if you want to get paticular data of particular fields only
print(csv_1.loc[[0,1],["std_name","std_roll"]])

# if you want to git full data
print(csv_1.loc[:,["std_name","std_roll"]])

print(csv_1.loc[[0,1],:])

print("\n")

# if you want to get particular data of patricular column and index
# --------------- use "iloc[row index,column index]" method 
print(csv_1.iloc[0,1])
print("\n")

# if you want to delelt one full row or column then use:
# ------------- "drop()" function
print(csv_1.drop("std_roll",axis=1))
print(csv_1.drop(0,axis=0))