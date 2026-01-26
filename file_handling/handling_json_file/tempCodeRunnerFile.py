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