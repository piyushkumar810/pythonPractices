# A student.json file contains the following fields:
# SRN, Name, M1, M2, M3
# Write a Python program to:
# 1️⃣ Create a JSON file
# 2️⃣ Write student data
# 3️⃣ Read the file
# 4️⃣ Display total and average marks

import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\student.json","w") as Wfile:

    students = [
    {"SRN": "pes101", "Name": "Piyush", "M1": 70, "M2": 60, "M3": 50},
    {"SRN": "pes102", "Name": "Prince", "M1": 80, "M2": 50, "M3": 90},
    {"SRN": "pes103", "Name": "Priyanshu", "M1": 50, "M2": 70, "M3": 60}
    ]

    json.dump(students,Wfile,indent=4)

    print("json file created successfully")

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\student.json","r") as Rfile:

    reader=json.load(Rfile)

    # print(reader)
    print("Name  Total  Average_Mark")
    for row in reader:
        total_marks=row["M1"]+row["M2"]+row["M3"]

        avg=total_marks/3

        print(row["Name"], total_marks, avg)
        


# question2

# 📘 SCENARIO-BASED QUESTION (EXAM STYLE)

# A Python program receives student details from a web service in the form of a JSON string.

# Each student record contains the following fields:
# SRN, Name, Marks (list of 3 subjects)

# Write a Python program to:
# Convert the student details from a Python dictionary into a JSON string
# Display the JSON string
# Convert the JSON string back into a Python dictionary
# Calculate and display the total and average marks

import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\student1.json","w") as wfile:

# ---------- STEP 1: Python object ----------
    student1 = {
        "SRN": "pes101",
        "Name": "Piyush",
        "Marks": [70, 60, 50]
    }
    
    # ---------- STEP 2: Convert Python object to JSON string ----------
    json_data = json.dumps(student1)
    print("JSON String:")
    print(json_data)
    
    # ---------- STEP 3: Convert JSON string back to Python object ----------
    python_data = json.loads(json_data)
    
    # ---------- STEP 4: Calculate total and average ----------
    total = sum(python_data["Marks"])
    average = total / len(python_data["Marks"])
    
    print("\nStudent Details:")
    print("Name:", python_data["Name"])
    print("Total Marks:", total)
    print("Average Marks:", average)
       