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