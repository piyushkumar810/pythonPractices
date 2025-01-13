# ------------------------ handling missing data using(dropena and fillena)---(lec-09)

# note--------------->  axis=0(for row) -----------and---------- > axis=1(for column)

import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv")
# print(csv_1)

# ----------------------------------------------------- dropena

# i want that the missing data should be dropped(means wherever "NaN" is written that field should be dropped)
# ye along row data ko drop kiya
# print(csv_1.dropna())
print("\n")

# but if i wnat that the data should be dropped along column--> we use "axis=1"
# print(csv_1.dropna(axis=1))

# in my employee record the 22 no record is field with "NaN"
# if i want to delete only that row which, all fields are field with "NaN" -->then use ="droppna(how="all")"
# print(csv_1.dropna(how="all"))
# if i want to delete all "NaN" records
# print(csv_1.dropna(how="any"))


# if i want to delete null data along particular column
# print(csv_1.dropna(subset=["Employee Salary"])) 


# print(csv_1.dropna(inplace=True))

# if you want to delete only that row or column which jitna ki thresh diya hua hai value (that means the row which consist of multiple null value will not be deleted)
# print(csv_1.dropna(thresh=2))

# --------------------------------------- fillena

# if you want to fill all null value with a particular value
# print(csv_1.fillna("python"))

# if you want that paticular column to be filled with specific value
# print(csv_1.fillna({"Employee Name": "pyhton", "Employee Salary": "c " , "Department":"java"}))

# if you want that the blank data should be filled with forward or backward data
# print(csv_1.fillna(method="ffill"))
# print(csv_1.fillna(method="bfill"))
# print(csv_1.fillna(method="ffill", axis=1))

# if you want to fill some value in place of all NaN value
# print(csv_1.fillna(12, inplace=True))
# print(csv_1)

