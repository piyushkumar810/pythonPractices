#---------------- question set

# Q1️⃣ Fetch and display all student data
# Q2️⃣ Display names of students who scored more than 80
# Q3️⃣ Count total number of students
# Q4️⃣ Find student with highest marks
# Q5️⃣ Increase marks of every student by 5
# Q6️⃣ Save updated data into a new JSON file

'''
✅ STEP 0: THINKING PATTERN (VERY IMPORTANT)

Before writing code, think:

1️⃣ JSON file → need json module
2️⃣ Read file → open()
3️⃣ Convert JSON → Python → json.load()
4️⃣ Data type → list of dictionaries
'''

# Q1️⃣ Fetch and display all student data
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)

    # print(reader)  #not well structured so we used for loop

    for lst in reader:
        print(lst)



# Q2️⃣ Display names of students who scored more than 80
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)

    # print(reader)  #not well structured so we used for loop

    for lst in reader:
        print(lst)

        if lst["marks"]>80:
            print(lst["name"])

# Q3️⃣ Count total number of students
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)
    print("Total students:", len(reader))
    # ------------------------- or
    # c=0
    # for lst in reader:
    #     c+=1
    # print("total no of records", c )



# Q4️⃣ Find student with highest marks
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)

    highest=reader[0]
    for lst in reader:
        if lst["marks"]>highest["marks"]:
            highest=lst
    
    print(highest)


# Q5️⃣ Increase marks of every student by 5
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)
    
    for lst in reader:
        lst["marks"]=lst["marks"]+5
        print(lst)



# Q6️⃣ Save updated data into a new JSON file
import json

with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\student.json",'r') as std:
    reader=json.load(std)
    
    new_student=[]
    for lst in reader:
        lst["marks"]=lst["marks"]+5
        new_student.append(lst)

    print(new_student)
    with open(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\file_handling\handling_json_file\updated_student","w") as new_std:

        json.dump(reader,new_std,indent=4)


# Q7📌 Group students by age and display count for each age 
'''🧠 STEP-BY-STEP THINKING
1 Read JSON
2 Create empty dictionary
3 Age → KEY
4 Count → VALUE
5 Update count using loop'''

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


# Q8)Find average marks of students whose age is ≥ 20