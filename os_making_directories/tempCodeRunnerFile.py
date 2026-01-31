import os

# base path and location where you want to create folder
base_path=r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices"

folders=[
    "Best_senario_based_question_all_units\unit_1",
    "Best_senario_based_question_all_units\unit_2",
    "Best_senario_based_question_all_units\unit_3",
    "Best_senario_based_question_all_units\unit_4"
]

for folder in folders:
    full_path=os.path.join(base_path,folder)
    os.makedirs(full_path,exist_ok=True)

print("All folders created successfully at specifid location!")
