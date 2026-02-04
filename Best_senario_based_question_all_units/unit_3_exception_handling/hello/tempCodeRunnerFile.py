
import csv

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\employee.csv","r") as Rfile:
    reader=csv.reader(Rfile)

    header=next(reader)
    print("Employee Name   Total Salary    Average Salary")

    for row in reader:
        name = row[1]
        basic = int(row[2])
        hra = int(row[3])
        da = int(row[4])

        total_salary=basic+hra+da

        average_salary=total_salary//3

        print(name, total_salary,average_salary)

