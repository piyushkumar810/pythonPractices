# Q) a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
#    1. write a program to seperate the following string into comma(,) seperated value.
#    2. write a program to sort string alphabetically in python.
#    3. write a pogram to remove the given character from a string ("BRB").

#    4. write a pogram to remove dot(.) from the following string.
#    5. write a program to check the number of occurrence of "O".

a="OOTD.YOLO.ASAP.BRB.GTG.OTW"

# 1st
seprate=a.replace(".", ",")
print(seprate)
print()

# 2nd
repl_str=a.replace(".","")
print(repl_str)
sort_str=sorted(repl_str)
print(sort_str)
print()

# 3rd
remov_char=a.replace(".BRB", "")
print(remov_char)
print()

# 4th
remo_dot=a.replace(".", "")
print(remo_dot)
print(type(remo_dot))
print()

# 5th
count_occurrence=a.count("O")
print(count_occurrence)