import os

# ----------------renaming the text file
# os.rename("Projects/clear_the_folder/clutterFolder/myText.txt", "Projects/clear_the_folder/clutterFolder/18.txt")

# --------------displaying all the files present in that folder
'''files=os.listdir("Projects/clear_the_folder/clutterFolder")
for file in files:
    print(file)'''

# -------------displaying all the file which which ends with .jpg
'''files=os.listdir("Projects/clear_the_folder/clutterFolder")
for file in files:
    if file.endswith(".JPG"):
        print(file)'''

# ---------------back to question
# Q) rename all the JPG image to 1.JPG, 2.Jpg ... n.JPG
files=os.listdir("Projects/clear_the_folder/clutterFolder")
# i=1
for file in files:
    if file.endswith(".JPG"):
        # os.rename(f"Projects/clear_the_folder/clutterFolder/{file}", f"Projects/clear_the_folder/clutterFolder/{i}.JPG")
        # i+=1
        print(file)