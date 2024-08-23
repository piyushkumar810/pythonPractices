import os
folders=os.listdir("multiple_file_program/os_module/data")

print(folders)

#-------------------------- tell you directory name 
# print(os.getcwd())

# printing it one - by - one
for folder in folders:
    print(folder)
    print(os.listdir(f"multiple_file_program/os_module/data/{folder}"))