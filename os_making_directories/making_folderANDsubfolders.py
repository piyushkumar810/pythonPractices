import os

# base path and location where you want to create folder
base_path="C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices"

folders=[
    "Best_senario_based_question_all_units\\unit_1",
    "Best_senario_based_question_all_units\\unit_2",
    "Best_senario_based_question_all_units\\unit_3",
    "Best_senario_based_question_all_units\\unit_4"
]

for folder in folders:
    full_path=os.path.join(base_path,folder)
    os.makedirs(full_path,exist_ok=True)

print("All folders created successfully at specifid location!")

'''
📌 Important

-> Use raw string r"" for Windows paths
      if you will not use r"" formate and you are using "/","\" single front slace or back slase then it will give you an error and folder creation unseccessful.

exist_ok=True avoids errors if folder already exists
'''

# ------------------------------------- you can do this also -------------------------------

import os

# main directory
main_dir = "C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\file_handling"

# sub-directories
sub_dirs = [
    "handling_csv_file",
    "handling_excel_file",
    "handling_json_file",
    "handling_text_file",
    "handling_xml_file"
]

# create main directory
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

# create sub-directories
for folder in sub_dirs:
    path = os.path.join(main_dir, folder)
    if not os.path.exists(path):
        os.mkdir(path)

print("Directory structure created successfully!")

# -----------need to know concepts
'''
🧠 Explanation (Viva Ready)

os.mkdir() → creates one directory
os.path.exists() → checks if directory already exists
os.path.join() → joins paths safely (OS independent)


📌 Common Exam Questions

Q: Difference between mkdir() and makedirs()?
mkdir() → creates single directory
makedirs() → creates parent + child directories
'''