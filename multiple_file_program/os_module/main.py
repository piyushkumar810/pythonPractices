# ------------------------------working with os module in pyhton

import os

if(not os.path.exists("multiple_file_program/os_module/data")):
    os.mkdir("multiple_file_program/os_module/data")

for i in range(0,10):
    os.mkdir(f"multiple_file_program/os_module/data/Day{i+1}")