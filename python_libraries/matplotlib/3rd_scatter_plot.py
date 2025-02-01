# scatter plot:- the data will be scattered at the different-different points. 
                #  this is useful when you are plotting the graph between numbers to numbers (means x and y axis both will be number)

import matplotlib.pyplot as plt
import numpy as np

virat_kohli=[2016,2017,2018,2019,2020,2021,2022,2023,2024]
t_20_score=[1110, 980, 740, 690, 750, 500, 340, 200, 160]
col=["red", "green", "blue", "pink", "black", "gray", "yellow", "brown"]
color=np.random.choice(col)

plt.scatter(virat_kohli,t_20_score, marker="*", cmap="viridis", c=color)
# plt.colorbar()
# plt.show()

# ------------------------------------- working with original data 
import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv"
df = pd.read_csv(file_path)

# Clean column names by stripping spaces
df.columns = df.columns.str.strip()

# Drop rows with missing Employee Salary or Performance Score
df = df.dropna(subset=["Employee Salary", "Performance Score"])

# Convert Employee Salary to float
df["Employee Salary"] = df["Employee Salary"].astype(float)

# Convert Performance Score to float (to preserve decimal values)
df["Performance Score"] = df["Performance Score"].astype(float)

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df["Performance Score"], df["Employee Salary"], color='blue', alpha=0.6, edgecolors="black")

# Labels and title
plt.xlabel("Performance Score")
plt.ylabel("Employee Salary")
plt.title("Performance Score vs Employee Salary")
plt.grid(True)

plt.show()
