# ------------------------------working with os module in pyhton

import os

if(not os.path.exists("multiple_file_program/os_module/data")):
    os.mkdir("multiple_file_program/os_module/data")

for i in range(0,10):
    # os.mkdir(f"multiple_file_program/os_module/data/Day{i+1}")
    # -------------------------renaming folders
    # os.rename(f"multiple_file_program/os_module/data/Day{i+1}", f"multiple_file_program/os_module/data/Tutorial{i+1}")
    # -------------------------suppose you want to give one space between tutorial and number
    os.rename(f"multiple_file_program/os_module/data/Tutorial{i+1}", f"multiple_file_program/os_module/data/Tutorial {i+1}") 