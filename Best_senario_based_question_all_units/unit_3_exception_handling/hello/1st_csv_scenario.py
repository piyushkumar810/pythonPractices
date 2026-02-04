# 📘 NEW PRACTICE QUESTION (PESU-STYLE)

# An employee.csv file contains the fields:
# EmpID, Name, Basic, HRA, DA
# Write a Python program to:
# Read the CSV file
# Calculate Total Salary = Basic + HRA + DA
# Display Employee Name, Total Salary, and Average Salary

import csv

file_path = r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\employee.csv"

# ---------- STEP 1: WRITE DATA TO employee.csv ----------
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["EmpID", "Name", "Basic", "HRA", "DA"])
    writer.writerow(["pes101", "Piyush", 70000, 6000, 5000])
    writer.writerow(["pes102", "Prince", 80000, 5000, 9000])
    writer.writerow(["pes103", "Priyanshu", 50000, 7000, 6000])

print("employee.csv created and data inserted successfully\n")


# ---------- STEP 2: READ FILE & CALCULATE ----------
with open(file_path, "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip header
    print("Employee Name   Total Salary    Average Salary")

    for row in reader:
        name = row[1]
        basic = int(row[2])
        hra = int(row[3])
        da = int(row[4])

        total_salary = basic + hra + da
        average_salary = total_salary / 3

        print(name, total_salary, round(average_salary, 2))

# ---------------------- working with dics reader
import csv

file_path = r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\employee.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    print("Employee Name   Total Salary   Average Salary")

    for row in reader:
        name = row["Name"]
        basic = int(row["Basic"])
        hra = int(row["HRA"])
        da = int(row["DA"])

        total = basic + hra + da
        average = total / 3

        print(name, total, round(average, 2))
