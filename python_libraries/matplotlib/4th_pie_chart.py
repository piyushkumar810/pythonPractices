# ------------------------------------ pie chart
'''
What is a Pie Chart?
A pie chart is a circular chart divided into slices to illustrate proportions of different categories in a 
dataset. Each slice represents a percentage of the total.

Why Use a Pie Chart in Data Analysis?
✅ Shows Proportion & Distribution:
        Helps understand which category has the largest share.
        Example: Market share of mobile brands.

✅ Easy to Interpret:
        Provides a quick visual summary of data.

🚫 Limitations:
        Not ideal for large datasets (too many slices make it cluttered).
        Difficult to compare small differences between categories.

''' 

import matplotlib.pyplot as plt

brands = ["OnePlus", "Apple", "Vivo", "Redmi", "Samsung"]
users = [13, 25, 22, 18, 22]

# important agar kisi brand ko highlight karna hai use ("explode and inside that jisko highlight karna hai uska value increase karke de do")
ex=[0,0.1,0,0,0]

# Corrected plt.pie() arguments
plt.figure(figsize=(7, 7))  # Set figure size
plt.pie(users, labels=brands, autopct="%1.1f%%", startangle=140, colors=["red", "blue", "green", "orange", "purple"], explode=ex, shadow=True)
# autopct =>(gives you values inside graph for clear understanding) ex:- "%.2f", "%1.1f%", "%1.1f%%"
# startangle =>pie chart ka starting ho woo kis angle se ho


# Title
# plt.title("Market Share of Smartphone Brands")

# plt.show()


# ------------------------------------- working with real data
import pandas as pd

file_path = "C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv"
df = pd.read_csv(file_path)
print(df)

# Clean column names by stripping spaces (if any)
df.columns = df.columns.str.strip()

# Drop rows with missing Employee Salary or Performance Score
df = df.dropna(subset=["Employee Name", "Performance Score"])

plt.figure(figsize=(7, 7))
plt.pie(df["Performance Score"], autopct="%1.1f%", startangle=110, colors=["red", "blue", "green", "orange", "purple"])

plt.title("performance score of employees")
plt.show()