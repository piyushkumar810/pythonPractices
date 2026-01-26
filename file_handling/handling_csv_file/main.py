'''
| Task       | Think                           |
| ---------- | ------------------------------- |
| Read CSV   | `csv.reader` / `csv.DictReader` |
| Row access | list OR dictionary              |
| Filter     | `if`                            |
| Count      | counter                         |
| Aggregate  | sum                             |
| Write CSV  | `csv.writer` / `DictWriter`     |

'''

# PROGRAM 1: READ & DISPLAY CSV (BASE)
import csv
with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\student.csv","r") as data:
    read1=csv.DictReader(data)

    for row in read1:
        print(row)


# ✅ PROGRAM 2: STUDENTS WITH MARKS > 80
import csv
with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\student.csv","r") as data:
    read1=csv.DictReader(data)

    for row in read1:
        if(int(row["marks"])>80):
            print(row)

# ✅ PROGRAM 3: COUNT TOTAL STUDENTS
import csv
with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\student.csv","r") as data:
    read1=csv.DictReader(data)
    count=0
    for row in read1:
        count+=1
    print(count)

# ✅ PROGRAM 4 (MEDIUM): FIND TOPPER
import csv

topper = None
max_marks = -1

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\student.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = int(row["marks"])
        if marks > max_marks:
            max_marks = marks
            topper = row

print("Topper:", topper["name"], "Marks:", topper["marks"])


# ✅ PROGRAM 5 (ADVANCED): CREATE NEW CSV (marks ≥ 80)
import csv

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\student.csv", "r") as infile, \
     open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_csv_file\filtered_students.csv", "w", newline="") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if int(row["marks"]) >= 80:
            writer.writerow(row)

print("Filtered CSV created successfully")


