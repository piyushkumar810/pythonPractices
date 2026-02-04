
import csv

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\student.txt","w") as file:
    writer=csv.writer(file)

    row=["SRN","NAME", "M1", "M2", "M3"]
    writer.writerow(row)
    print("row created successful")

    row1=["pes101", "Piyush", 70,60,50]
    row2=["pes102", "Prince", 80,50,90]
    row3=["pes103", "Priyanshu", 50,70,60]
    rows=[row1,row2,row3]
    writer.writerows(rows)
    print("data inserted successful")

    with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello\student.txt","r") as Rfile:
        reader=csv.reader(Rfile)

        for row in reader:
            print(row)
