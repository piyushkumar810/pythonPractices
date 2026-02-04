
import csv

# ---------- STEP 1: CREATE student.csv FILE ----------
with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\student.txt", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["SRN", "Name", "M1", "M2", "M3"])

    # Student records
    writer.writerow(["pes101", "Piyush", 70, 60, 50])
    writer.writerow(["pes102", "Prince", 80, 50, 90])
    writer.writerow(["pes103", "Priyanshu", 50, 70, 60])

print("student.csv file created successfully\n")

