# 2. win32gui
# The win32gui module focuses on Windows GUI (Graphical User Interface) operations, providing tools to
#  manage windows, dialogs, and other GUI components.

# Key Features:
# Manipulating and controlling windows.
# Creating and managing dialog boxes.
# Accessing and handling GUI events.

import win32gui
hwnd = win32gui.GetForegroundWindow()
title = win32gui.GetWindowText(hwnd)
print("Active Window Title:", title)
