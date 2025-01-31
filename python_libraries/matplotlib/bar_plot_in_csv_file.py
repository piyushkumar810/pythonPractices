import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv"
df = pd.read_csv(file_path)

'''
----------------------- Issues in this file data:
CSV Formatting Issues:-
       --> The dataset you shared has missing values, which might cause errors when plotting.
       --> There’s an extra empty row (NaN values at index 22), which could be causing issues.


Column Name Issues:-
        -->CSV files may have spaces in column names. Instead of df["Employee Salary"], 
            try df["Employee Salary"].astype(float) to ensure proper data type handling.

            
Missing Value Handling:-
        --> If Employee Salary has missing values (NaN), you need to handle them before plotting.
'''

# Clean column names by stripping spaces (if any)
df.columns = df.columns.str.strip()

# Drop rows with missing Employee Salary or Department
df = df.dropna(subset=["Employee Salary", "Department"])
print(df)
# print(type("Employee Salary"))

# Convert Employee Salary to float (if necessary)
df["Employee Salary"] = df["Employee Salary"].astype(float)

# # Plot the bar chart
# plt.figure(figsize=(10, 5))
# plt.bar(df["Department"], df["Employee Salary"], color="skyblue")
# plt.xticks(rotation=45)  # Rotate department labels for better readability
# plt.xlabel("Department")
# plt.ylabel("Employee Salary")
# plt.title("Employee Salary by Department")
# plt.show()
