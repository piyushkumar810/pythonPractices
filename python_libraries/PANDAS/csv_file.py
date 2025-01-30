# ------------------------ python pandas csv file (lec - 06)

# difference between CSV file and xls(excel) file formates :
'''
ans->
CSV file -> csv formate is a plain text formate in which values are seperated by commas(comma seperated values).

excel file-> it is a excel sheet binary file formate which holds information about all the worksheets in a 
             file, including both content and formatting.
             
          #    to work with excel sheet you need to doownload
                pip install openpyxl

          #    and if you want to use it ?
                variable_name=pd.read_excel("address of that excel sheet")
'''

# write csv file
import pandas as pd

dic={"S_name":["suraj","dhiraj","piyush","sikender","ritlal"],
     "S_roll":[48,10,28,44,35],
     "S_course":["BA","ITI","BCA","BCA","BBA"],
     "S_marks":[395,350,280,400,405],
     "S_college":["ignou","govinda","markham","markham","ananda"]}

var=pd.DataFrame(dic)

print(var)

# var.to_csv("Student_Record.csv")

# ? ----------if want to hide/change row index then there is a parameter
# var.to_csv("Student_Record1.csv", index=False) 
# var.to_csv("Student_Record1.csv", index=[1,2,3,4.5])

# ?-----------if you want to change/hide column index then use
# var.to_csv("Student_Record2.csv", index=False, header=False)
var.to_csv("Student_Record2.csv", index=False, header=["std_name","std_roll","std_course","std_mark","std_vollege"])
