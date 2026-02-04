# 🔹 UNIT–3
# Exception Handling, File I/O, Modules
# Section A – Exceptions

'''
Q1.Write a program to:
Create custom exception NegativeBalanceError
Raise it when withdrawal exceeds balance
'''
# -------------- solution
'''
-> in question is it said to use class?
Short, clear answer: YES, it is IMPLIED.

1️⃣ “Create custom exception”
In Python, a custom exception MUST be a class that inherits from Exception.

So this line automatically implies:
class NegativeBalanceError(Exception):
    pass
'''
class NegativeBalanceError(Exception):
    pass

class Bank:
    def __init__(self,balance):
        self.balance=balance

    def withdrawal(self,withdraw):
        if(withdraw>self.balance):
            raise NegativeBalanceError("insufficient balance")
        
        else:
            print(f"total balance in your account {self.balance}")
            print(f"after withdrawing {withdraw}")
            self.balance=self.balance-withdraw
            print(f"the remaining balance is {self.balance}")
try:
    obj=Bank(50000)
    obj.withdrawal(30000)
    obj.withdrawal(60000)

except NegativeBalanceError as neg:
    print("insufficient balance")
    





'''
Q2.Write a Python program that:
Handles ValueError, ZeroDivisionError
Uses else and finally blocks
'''
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    result = num1 // num2
    print("Result:", result)

except ValueError:
    print("ValueError: Invalid integer input")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

else:
    print("Division successful")

finally:
    print("Execution completed")

    
















# Section B – File Handling (High Probability)
'''
Q3.Write a Python program to:
Read a CSV file containing ID, Name, Salary
Display highest paid employee
'''

'''
Q4.Write a program to:
Read JSON file
Convert it to CSV
'''

'''
Q5.Write a Python program using pickle to:
Serialize employee objects
Deserialize and display them
'''

# Section C – Modules
'''
Write a program using os module to:
Create a directory
Rename a file
Delete empty directories

import sys
print(sys.argv)

(Assume arguments passed)
'''
import os

# creating a directory
path=(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_3_exception_handling\hello")
os.makedirs(path)

# renaming a file
old_name="piyush.txt"
new_name="kumar.txt"
os.rename(old_name,new_name)

# deletion folder
os.rmdir(path)


# ---------------------------------- full practice
import os

# 1️⃣ Create a directory
dir_name = "test_dir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print("Directory created:", dir_name)
else:
    print("Directory already exists")

# 2️⃣ Create a file inside the directory
file_path = os.path.join(dir_name, "sample.txt")
with open(file_path, "w") as f:
    f.write("Hello PES University")

print("File created:", file_path)

# 3️⃣ List files in directory
print("Contents of directory:", os.listdir(dir_name))

# 4️⃣ Rename the file
new_file_path = os.path.join(dir_name, "renamed_sample.txt")
os.rename(file_path, new_file_path)
print("File renamed")

# 5️⃣ Remove the file
os.remove(new_file_path)
print("File removed")

# 6️⃣ Delete empty directory
os.rmdir(dir_name)
print("Directory deleted")


'''
| Function          | Purpose                         |
| ----------------- | ------------------------------- |
| `os.mkdir()`      | Create **one** directory        |
| `os.makedirs()`   | Create **nested** directories   |
| `os.rmdir()`      | Delete **empty** directory      |
| `os.removedirs()` | Delete nested empty directories |
'''







# ---------------------------- (pyq questions)
'''
Q3 (a)
Import specific system modules to:
Get the current working directory
List all files and directories in the current directory
Delete a file
Add days to the current date
'''
import os
from datetime import datetime, timedelta

# 1️⃣ Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# 2️⃣ List all files and directories in current directory
print("Files and Directories:")
print(os.listdir(cwd))

# 3️⃣ Delete a file (assume file exists)
file_name = "sample.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted:", file_name)
else:
    print("File does not exist")

# 4️⃣ Add days to the current date
today = datetime.now()
future_date = today + timedelta(days=10)

print("Today's date:", today.date())
print("Date after 10 days:", future_date.date())



'''
Q3 (b)
Handle the following exceptions:
Attempt to open a non-existing file
Create a custom exception InvalidAgeError raised if age < 18
Zero division error
'''
import csv

# 1️⃣ Handle non-existing file
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found")


# 2️⃣ Custom exception for age
class InvalidAgeError(Exception):
    pass

class Age:
    def __init__(self, age):
        self.age = age

    def check_age(self):
        if self.age < 18:
            raise InvalidAgeError("Age must be 18 or above")
        else:
            print(f"Correct age: {self.age}")
try:
    obj = Age(12)
    obj.check_age()

except InvalidAgeError as iv:
    print("Invalid age:", iv)



# 3️⃣ Handle ZeroDivisionError
try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")



'''
Q3 (c)
A student.csv file is created with fields:
SRN, Name, M1, M2, M3
Write a Python program to:
Read the file
Display total and average marks of each student
'''
import csv

# ---------- STEP 1: CREATE student.csv FILE ----------
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["SRN", "Name", "M1", "M2", "M3"])

    # Student records
    writer.writerow(["pes101", "Piyush", 70, 60, 50])
    writer.writerow(["pes102", "Prince", 80, 50, 90])
    writer.writerow(["pes103", "Priyanshu", 50, 70, 60])

print("student.csv file created successfully\n")


# ---------- STEP 2: READ FILE & CALCULATE TOTAL & AVERAGE ----------
with open("student.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)   # Skip header
    print("SRN   Name        Total   Average")

    for row in reader:
        srn = row[0]
        name = row[1]
        m1 = int(row[2])
        m2 = int(row[3])
        m3 = int(row[4])

        total = m1 + m2 + m3
        average = total / 3

        print(srn, name, total, round(average, 2))
