# ---------------------------------------------- dictionary in python
student = {"name": "piyush",
           "roll" : 28,
           "course": "BCA"}
print(student)
print("your roll no =", student["roll"], "and your name is :", student["name"])
print("\n")

# ------------------------------------functions of dictionary
employees={"Ename": "suresh",
           "Esalary":56000,
           "Eid":51000235}
# 1st --> len()
print(len(employees))

# 2nd --> type()
print(type(employees))

# 3rd --> get()
a=employees.get("Esalary")
b=employees.get("Ename")
print(a)
print(b)

# 4th --> key()
c=employees.keys()
print(c)

# 5th --> adding new element in dictonary
employees["Estatus"]="good"
print(employees)

# 6th --> values()
d=employees.values()
print(d)

# 7th --> pop()
employees.pop("Eid")
print(employees)

# 8th --> clear()
employees.clear()
print(employees)