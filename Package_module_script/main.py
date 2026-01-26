'''🧠 PART 3 — CODING EXAMPLES (CLEAN & SIMPLE)
📁 Project Structure (VERY IMPORTANT)
project/
│
├── main.py
│
└── math_pkg/
    ├── __init__.py
    ├── add.py
    └── sub.py
'''

'''# 🔹 add.py
def add(a, b):
    return a + b

# 🔹 sub.py
def sub(a, b):
    return a - b

🔹 __init__.py
from .add import add
from .sub import sub

🔹 main.py (ABSOLUTE IMPORT)
from math_pkg import add, sub

print(add(10, 5))
print(sub(10, 5))


✅ This is EXAM-SAFE + INDUSTRY-SAFE

🔹 Relative import example (inside package only)

Inside math_pkg/test.py:

from .add import add

print(add(2, 3))


📌 Will FAIL if run directly ❌
📌 Works when package is imported ✔️

📝 PERFECT 5-MARK EXAM ANSWER

A package in Python is a directory containing multiple modules and an __init__.py file. The __init__.py file marks the directory as a package and may contain initialization code. Python supports absolute imports using full module paths and relative imports using dot notation. Absolute imports are preferred, while relative imports are used within packages.

🎯 FINAL CONFIDENCE LINE

File → module
Folder → package
Dot → relative import
Full path → absolute import'''