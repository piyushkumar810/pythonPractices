# ------------------------ read csv file- with python pandas(lec-07)

import pandas as pd

csv_1=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv")
# read_csv("path") -> it will read your csv file
# print(csv_1)
# print("\n")


# if you want to fetch row data
csv_2=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", nrows=3)
# print(csv_2)
# print("\n")


# if you want to get column or columns
# csv_3=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", usecols=["std_vollege"])
# get multiple columns
# csv_3=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", usecols=["std_vollege","std_mark"])
# if you dont want to give name then you can use column index also
csv_3=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", usecols=[1,3])
# print(csv_3)
# print("\n")


# if you want to skip the desired row which you want to skip
# skiprows=[the row you want to skip]  (issese ek row upper shift ho rahi hai)
csv_4=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", skiprows=[0])
# print(csv_4)
# print("\n")

# if you want to change heading 
# ex:- allot [dhiraj,10,ITI,350,govinda ] in place of (std_name,roll,course,mark..) then the attribute is "header"
csv_5=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", header=2)
print(csv_5)
# ----------------explanation
'''
  std_name  std_roll std_course  std_mark std_vollege
0     suraj        48         BA       395       ignou  --> this is 1st row
1    dhiraj        10        ITI       350     govinda  --> this is 2nd row 
2    piyush        28        BCA       280     markham  --> this is 3rd row
3  sikender        44        BCA       400     markham  --> this is 4th row
4    ritlal        35        BBA       405      ananda  --> this is 5th row

but above dhiraj every column will be shifted above like vanished
'''
print("\n")


# if you want to change the name of header
# using this the header will come down
# csv_6=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", names=["col1", "col2", "col3", "col4", "col5"])
# print(csv_6)
# if you want to remove header
# use header=none
csv_6=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", header=None,names=["col1", "col2", "col3", "col4", "col5"] )
print(csv_6)
print("\n")


# if you want to change the data type of the std_roll
csv_7=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Student_Record2.csv", dtype={"std_roll":"float"})
print(csv_7)