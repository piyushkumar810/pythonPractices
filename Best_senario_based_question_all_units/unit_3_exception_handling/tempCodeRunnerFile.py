
import os
from datetime import datetime, timedelta

# 1️⃣ Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# 2️⃣ List all files and directories in current directory
print("Files and Directories:")
print(os.listdir(cwd))

# 3️⃣ Delete a file (assume file exists)
file_name = "sample.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted:", file_name)
else:
    print("File does not exist")

# 4️⃣ Add days to the current date
today = datetime.now()
future_date = today + timedelta(days=10)

print("Today's date:", today.date())
print("Date after 10 days:", future_date.date())
