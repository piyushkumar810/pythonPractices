# Q1️⃣ Fetch and display all student data
# Q2️⃣ Display names of students who scored more than 80
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student_dict.json",'r') as std:
    reader=json.load(std)

    # print(reader)  #not well structured so we used for loop

    for key,val in reader.items():
        # print(key,val)
        if(val["marks"]>80):
            print(val["name"])


'''
Variable    	Contains
key	            "S101"
val	            {"name": "Amit", "age": 20, "marks": 85}

👉 Marks is inside val, not key'''



# 🔥 TOUGH QUESTION 3
# 📌 Create a new JSON dictionary containing only students whose age ≥ 20
# and save it to filtered_students.json

import json 
with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student_dict.json", "r") as data:
    reader=json.load(data)

    filtered_student={}
    for k,v in reader.items():
        # print(k,v)
        if(v["age"]>=20):
            filtered_student[k]=v
    
    with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\filtered_students.json", "w") as new_rec:
        json.dump(filtered_student, new_rec, indent=4)