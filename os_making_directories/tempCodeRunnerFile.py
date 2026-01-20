import os

# base path and location where you want to create folder
base_path=r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices"

folders=[
    "file_handling\handling_csv_file",
    "file_handling\handling_excel_file",
    "file_handling\handling_json_file",
    "file_handling\handling_text_file",
    "file_handling\handling_xml_file"
]

for folder in folders:
    full_path=os.path.join(base_path,folder)
    os.makedirs(full_path,exist_ok=True)

print("All folders created successfully at specifid location!")