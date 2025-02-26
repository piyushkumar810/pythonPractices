# ---------------------------------- groupBy() function in python -------------------------------------

import pandas as pd

var=pd.DataFrame({
    "name": ["a","b","c","d","a","b","a","b","a","c","c","d"],
    "s_1":[12,13,14,12,13,15,23,16,10,13,12,34],
    "s_2":[23,24,25,27,28,19,32,34,37,39,35,56]
})

print(var)

var_new=var.groupby("name")
print(var_new)

for x,y in var_new:
    print(x)
    print(y)
    print()


# agar koi particular group chaiya tho use (get_group())
var_new=var_new.get_group("a")

print(var_new)