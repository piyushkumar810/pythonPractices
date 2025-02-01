import matplotlib.pyplot as plt

restaurent=["Day1", "Day2", "Day3", "Day4","Day5"]
people_arrived_week1=[300,420,250,230,400]
people_arrived_week2=[500,450,300,250,320]

# plt.plot(restaurent,people_arrived_week1, marker="o",ls="dashed", color="b", label="week1")
# plt.plot(restaurent,people_arrived_week2, marker="h",ls="dashdot", color="r", linewidth=2, label="week2")
# plt.legend()
# plt.show()

# ------------------------------------- importing file
import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\piyush kumar\\Downloads\\Employee_Records.csv"
data=pd.read_csv(file_path)
# print(data)
# print(type(data))
# print()

df=pd.DataFrame(data)
print(df)

# Clean column names by stripping spaces (if any)
df.columns = df.columns.str.strip()

# Drop rows with missing values
df = df.dropna(subset=["Employee Salary", "Employee Name"])

# Convert Employee Salary to float
df["Employee Salary"] = df["Employee Salary"].astype(float)

# Plot the Employee Salary against Employee Name
plt.figure(figsize=(12, 6))  # Set figure size for better readability
plt.plot(df["Employee Name"], df["Employee Salary"], marker="o", linestyle="-", color="b")

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Labels and title
plt.xlabel("Employee Name")
plt.ylabel("Employee Salary")
plt.title("Employee Salary Trend")

plt.show()