#----------------------------- how to delete and insert data in pandas(lec-05)

import pandas as pd

var=pd.DataFrame({"A": [1,2,3,4,5], "B": [9,8,7,6,5]})

# insert()- to insert the data inside dataFrame it consist of three parameter(kaha per, column name, value)
var.insert(1,"C",[4,5,6,7,8])
'''
note:-

? if you want to insert a new column which has less data or more data than "A" and "B" ex:
var.insert(2,"D",[7,90,56])

------------output---------------
value error
Length of values (3) does not match length of index (5)

'''

# coping the data (using slicing)
var["copy_data"]=var["A"][0:3]


# ----------------------------------------------deleting the data
# pop()--> pop method consist of one column that which column you want to delete ("column name")
var.pop("C")

# del keyword
del var["B"]


print(var)
print(type(var))