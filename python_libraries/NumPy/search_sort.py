# -------------------------- search, sort, search Sorted, filter  (lec-14)

# -----------search
import numpy as np
var=np.array([2,4,6,7,10,12,13,16])

x1=np.where(var==12)
# it will search in which index the value 12 lies
print(x1)
print()

x2=np.where((var%2)==0)
# ye dega kon kon sa index per reminder 0 mil rha hai
print(x2)
print("\n")

# ---------- "search sorted" array (which perform a binary search in the array, and return the index where the specified value would be inserted to maintained the search order)
var1=np.array([2,4,6,7,10,12,13,16])

x2=np.searchsorted(var1, 5)
# it returns the index value where should this value be inserted
print(x2)
print()

# you can insert a list also
x3=np.searchsorted(var1, [5,6,7] , side="right")
print(x3)
print()

# -------------------- sort array (ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending)
var2=np.array([3,7,0,1,12,56,2,5,203])
print(var2)
print()

x4=np.sort(var2)
print(x4)
print()

# sorting string
var3=np.array(['a', 't', 's', 'r', 'z', 'b', 'p'])
print(var3)
print()

x5=np.sort(var3)
print(x5)
print()

var4=np.array(['ashish', 'tulika', 'saloni', 'raja', 'zubar', 'babita', 'piyush'])
print(var4)
print()

x6=np.sort(var4)
print(x6)

# 2-d array
var5=np.array([[3,7,0],[1,12,56],[2,5,203]])
print(var5)
print()

x7=np.sort(var5)
print(x7)
print("\n")

# --------------- filter array (getting some element out of an existing array and creating a new array out of them.)
var6=np.array([4,6,8,0,2,4,35,54,56,32,45,467])
print(var6)
print()
x=[True,True,True,False,True,False,True,True,True,False,False,False]
filter_arr=var6[x]
print(filter_arr)
print(type(filter_arr))