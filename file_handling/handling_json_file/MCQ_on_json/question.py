#     🔹 MCQ 1: load vs loads
import json

data = '{"a": 10, "b": 20}'
result = json.loads(data)
print(type(result))

'''
What is the output?

A. <class 'str'>
B. <class 'list'>
C. <class 'dict'>
D. Error

✅ Answer: C
📌 loads() converts JSON string → Python dict
'''

# 🔹 MCQ 2: File-based JSON reading

'''Which function is used to read JSON data directly from a file object?

A. json.loads()
B. json.load()
C. json.read()
D. json.parse()

✅ Answer: B
'''


# 🔹 MCQ 3: Dictionary JSON iteration
for k, v in data.items():
    print(k, v)


'''Here data is loaded from a dictionary-based JSON.
What does k represent?

A. Entire JSON object
B. Student details
C. Student ID / key
D. Index number

✅ Answer: C'''

# 🔹 MCQ 4: Invalid JSON
'''Which of the following is INVALID JSON?

A.
{"a": 10, "b": 20}

B.
{"a": 10, "b": [1,2,3]}

C.
{'a': 10, 'b': 20}

D.
{"a": true}


✅ Answer: C
📌 JSON uses double quotes only
'''


# 🔹 MCQ 5: JSON data type mapping
'''
Which Python data type does a JSON array convert to?

A. Tuple
B. Set
C. List
D. Dictionary

✅ Answer: C
'''


# 🔹 MCQ 6: Sorting JSON data
'''
Which code correctly sorts students by marks (descending)?

A.
sorted(data, reverse=True)

B.
sorted(data, key="marks")

C.
sorted(data, key=lambda x: x["marks"], reverse=True)

D.
data.sort("marks")

✅ Answer: C
'''


# 🔹 MCQ 7: dump vs dumps
'''
Which statement is TRUE?

A. dump() returns a JSON string
B. dumps() writes JSON to a file
C. dump() writes Python object to file
D. dumps() reads JSON from file

✅ Answer: C
'''


# 🔹 MCQ 8: Indentation purpose
'''
json.dump(data, file, indent=4)


What is the purpose of indent=4?

A. Faster execution
B. Smaller file size
C. Better readability
D. Required for valid JSON

✅ Answer: C
'''


# 🔹 MCQ 9: JSON key type
'''
Which of the following is TRUE about JSON keys?

A. Keys can be integers
B. Keys can be lists
C. Keys must be strings
D. Keys can be tuples

✅ Answer: C
'''


# 🔹 MCQ 10: Nested JSON access
data = {
  "S101": {
      "name": "Amit",
      "marks": 85
  }
}
print(data["S101"]["marks"])

'''
Output?

A. "marks"
B. 85
C. Error
D. None

✅ Answer: B
'''


# 🔹 MCQ 11: Updating JSON data
'''
Which code correctly updates marks?

A.
data["marks"] = 90

B.
data["S101"]["marks"] = 90

C.
data["S101"].append(90)

D.
update(data["marks"])


✅ Answer: B
'''


# 🔹 MCQ 12: JSON + Exception handling (ADVANCED)
'''
Which exception is raised when JSON format is invalid?

A. TypeError
B. ValueError
C. json.JSONDecodeError
D. KeyError

✅ Answer: C'''