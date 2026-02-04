
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
       