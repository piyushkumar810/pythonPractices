'''
2.b. Given the multiline string
student_scores = """pes001 98 78 67
pes002 99 44 79
pes006 44 55 33
pes007 55 88 40
pes009 34 78 65"""
Each row has details of a student (srn, phy_marks, chem_marks,
math_marks) separated by a space n between.
Calculate the total marks of a particular student. Display the srn as the
key and the total marks as the value.
 
Expected Output:
    {'pes001': 243, 'pes002': 222, 'pes006': 132, 'pes007': 183, 'pes009': 177}

'''
student_scores = """pes001 98 78 67
pes002 99 44 79
pes006 44 55 33
pes007 55 88 40
pes009 34 78 65"""

result = {}

for line in student_scores.split('\n'):
    data = line.split()
    srn = data[0]
    marks = map(int, data[1:])
    result[srn] = sum(marks)

print(result)
