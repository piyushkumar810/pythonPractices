# ------------------------------------enumerate function in python

# problem faced before enumerate function
# we face diffuculties in iterating (list, tuple ..) using there indexes because here we have to take a temprory variable to see index 
# eg

marks=[12, 56, 32, 98, 12, 45, 1, 4]
index=0
for mark in marks:
    print(mark)
    if(index == 3):
        print("piyush, awesome ! ")
    index +=1

print("\n")
# this temprory variable problem is solved by enumerate function
# eg

marks1=[12, 56, 32, 98, 12, 45, 1, 4]
for i, mark1 in enumerate(marks1):
    print(mark1)
    if(i==3):
        print("piyush, awesome ! ")

print("\n")
# you can change the starting index 
# eg

courses=['BBA','BCA','MCA','MBA','BA','MA']
for idx, course in enumerate(courses, start=1):
    print(course + " index is " + idx)
    if(idx == 3):
        print("selected")

