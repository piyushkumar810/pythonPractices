# ------------------------------------ Replace and Interpolate in python pandas

import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv"
data=pd.read_csv(file_path)
print(data)

'''
# data.replace("Department 1", "piyush")
--------error-----------
data.replace("Department 1", "piyush") creates a new DataFrame but does not modify data directly.

-------------------------or----------------------------------
You need to either assign it back or use inplace=True.
# data.replace("Department 1", "piyush", inplace=True)
------------why------------
When you use inplace=True in a Pandas method, it modifies the DataFrame directly instead of returning a new one. 
This helps save memory and avoids the need for reassignment.

'''
# df=data.replace(inplace=1,value=22)
df=data.replace("Department 1","piyush")
# print(df)

df1=data.replace(["Department 1","Department 2","Department 3","Department 4"], 22)
print(df1)
print("\n")

# ---------use of regex
df2=data.replace("[A-Za-z]","python",regex=True)
print(df2)

'''
-------------- regex------
When you use regex=True in replace(), it tells Pandas that the first argument is a regular expression (regex) 
instead of an exact string. This allows for pattern-based replacements instead of simple text replacements.

# df2=data.replace("[A-Za-z]","python",regex=True)
whith this line of code it will replace example:
                                        jhon = pythonpythonpythonpython

# df2 = data.replace(r"\b[A-Za-z]+\b", "python", regex=True)
explanation:-

\b → Marks the start or end of a word.
[A-Za-z]+ → Matches entire words (one or more letters).
\b → Ensures only full words are matched, not parts of numbers or symbols.
Now, "Sales" becomes "python" instead of "pythonpythonpythonpython".

'''
print()
# replacing one column data using regular expression 
df3=data.replace({"Employee Name":"[A-Z]"},22,regex=True)
print(df3)