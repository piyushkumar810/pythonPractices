# remember
'''
| Function       | Converts                        |
| -------------- | ------------------------------- |
| `json.loads()` | JSON **string** → Python object |
| `json.dumps()` | Python object → JSON **string** |

'''

import json

json_data = '''
{
  "S101": {"name": "Amit", "age": 20, "marks": 85},
  "S102": {"name": "Neha", "age": 21, "marks": 92},
  "S103": {"name": "Rahul", "age": 19, "marks": 78},
  "S104": {"name": "Priya", "age": 20, "marks": 88},
  "S105": {"name": "Kiran", "age": 22, "marks": 67}
}
'''

student_record=json.loads(json_data)   # json data string mai tha i converted into python object and object is in the form of dictionary
# print(student_record)
# for key,val in student_record.items():
    # print(key,val)
    # now result is in dictionary


# Step 4: Perform operation (marks > 80) and save again in new file and data should be in string
filter_record={}
for key,val in student_record.items():
    if(val["marks"]>80):
        filter_record[key]=val

result_json=json.dumps(filter_record, indent=4)
print(result_json)




# -------------------------------- one easy concept but every one forget
# to add data inside list aand dictionary
'''
| Data Type      | Add Data            |
| -------------- | ------------------- |
| **List**       | `append()`          |
| **Dictionary** | `dict[key] = value` |

'''