# 1. win32api
# The win32api module provides access to core Windows API functions, including file handling, 
# system information, and basic GUI operations.

# Key Features:
# File and directory manipulation.
# Getting system and environment information.

import win32api

# it will display message in message box
win32api.MessageBox(0, "Hello, World!", "Win32 API", 0)

# get your computer name
print("Computer Name:", win32api.GetComputerName())

# it will get you all drive name created by-default or manully
drives = win32api.GetLogicalDriveStrings().split('\x00')
print("Drives:", drives)