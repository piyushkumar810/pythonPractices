import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)

    age_count={}
    for student in reader:
        age=student["age"]

        if age in age_count:
            age_count[age]+=1
        else:
            age_count[age]=1
    for age,count in age_count.items():
        print(f"{age}->{count} student")