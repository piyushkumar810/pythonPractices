# 1️⃣ What is a JSON file?
'''
JSON (JavaScript Object Notation) is a data format, very common in:

APIs
Web applications
Config files
Databases (MongoDB)
'''

{
  "name": "Piyush",
  "age": 21,
  "skills": ["Python", "Pandas"]
}

'''
In Python:
JSON looks like dictionary
JSON array looks like list of dictionaries
'''

'''
2️⃣ Why use Pandas for JSON?

Pandas helps to:

Read JSON files easily
Convert JSON → DataFrame
Analyze, filter, clean data
Export JSON back to file
'''

[
  {"id": 1, "name": "Amit", "marks": 85},
  {"id": 2, "name": "Riya", "marks": 90},
  {"id": 3, "name": "John", "marks": 78}
]

import pandas as pd
df=pd.read_json()