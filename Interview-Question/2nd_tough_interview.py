# ---------------- python interview question for Experienced users:---------------

# Q1) how to create a new column in pandas by using values from other columns?
'''
import pandas as pd
a=[1,2,3]
b=[2,3,5]

d={"col1":a, "col2":b}
df=pd.DataFrame(d)

print(df)
df["sum"]=df["col1"]+df["col2"]
df["substract"]=df["col2"]-df["col1"]
print(df)
'''

# Q2) what are the different functions that can be used by the groupby in pandas?
'''
the groupby() function in pandas cna be used with multiple aggregate functions.
--> some of which are sum(), mean(), count(), std().

'''

# Q3) how to select columns in pandas and add them in new dataframe? 
#      what if there are two columns with the same name?

'''
if df is a DataFrame in pandas, df.columns give the list of all columns.

we can then form new columns by selecting particular columns.

if there are two columns with same name then both columns get copied to the new dataframe.

example:

import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Selecting columns 'A' and 'C' to create a new DataFrame
df_new = df[['A', 'C']]
print(df_new)
'''

# Q4) how to delete a column or a group of column in pandas ?
'''
import pandas as pd

data={"roll":[25,26,27,28,30],
      "name":["priya", "pratham", "piyush", "parth", "parnav"],
      "marks":[340, 330, 380, 420, 390]
      }

df=pd.DataFrame(data)
df=df.drop(["roll"], axis=1)
print(df)
'''

# Q5) give the following dataframe drop rows having column values as A.
'''
while using dropna() function

example:-

import pandas as pd

# Create DataFrame
data = {
    "col1": [1, 2, 3],
    "col2": ["A", "B", "C"]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df, "\n")

# Drop NaN values (not necessary here since there are no NaNs)
df = df.dropna()

# Filter out rows where col1 is 1
df = df[df["col1"] != 1]

# Display modified DataFrame
print("Modified DataFrame:")
print(df)

'''

# Q6) given below the dataset find the highest paid player in each college in neach team.
'''
import pandas as pd

# Sample dataset with Indian names
data = {
    "Team": ["Mumbai Indians", "Mumbai Indians", "Mumbai Indians", 
             "Chennai Super Kings", "Chennai Super Kings", "Chennai Super Kings", 
             "Royal Challengers Bangalore", "Royal Challengers Bangalore"],
    
    "College": ["Delhi University", "Mumbai University", "Delhi University", 
                "Anna University", "Delhi University", "Anna University", 
                "Bangalore University", "Bangalore University"],
    
    "Player": ["Rohit Sharma", "Suryakumar Yadav", "Ishan Kishan", 
               "MS Dhoni", "Ravindra Jadeja", "Ruturaj Gaikwad", 
               "Virat Kohli", "KL Rahul"],
    
    "Salary": [160000000, 110000000, 150000000, 120000000, 130000000, 70000000, 170000000, 140000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find highest-paid player in each college for each team
highest_paid = df.loc[df.groupby(["Team", "College"])["Salary"].idxmax()]

# Display the result
print("Highest Paid Player in Each College for Each Team:")
print(highest_paid)

'''