# 🧠 What is a “Python Cell Script” (Plain English)

'''
A Python cell script means:
Writing and executing Python in small independent blocks (cells) instead of one long .py file.

This is most commonly done in:
Jupyter Notebook
JupyterLab
Google Colab
VS Code notebooks

Each block = one cell
'''


# 🔹 Why Cells Exist (Very Important)
'''
Traditional .py file:
Runs top → bottom
Every run starts fresh
Bad for experiments


Cell-based Python:
Run only what you want
Keep variables alive

Perfect for:
Learning
Data science
ML
Testing logic
Debugging
Visualization

👉 Cells = interactive Python
'''


# 🧩 Structure of a Notebook
'''
A notebook has cells, not lines.

Two main cell types:
Code Cell – runs Python
Markdown Cell – explanations, notes

▶️ Your First Code Cell (Conceptually)
a = 10
b = 20
a + b


👉 When you run the cell:
Python executes it
Last expression auto-prints
No print() needed
This is a cell superpower
'''


# 🔁 Cells Are NOT Independent (Critical Concept)
'''
Cells share memory.
Example:

Cell 1
x = 100

Cell 2
x + 50


✅ Works
Why? Same Python kernel (brain)

⚠️ Cell Order Matters (Exam + Real Life)

If you run Cell 2 before Cell 1:

x + 50


❌ NameError

Notebook rule:
Execution order > Visual order
Always watch the execution number like:

[1]  [2]  [5]

🧠 Kernel (The Brain Behind Cells)

Kernel = Python running in background
Restart kernel = everything wiped
Variables, imports, objects → gone
This explains 90% notebook bugs.
'''


# 🔄 Restart vs Run All
'''
Restart Kernel → fresh Python
Run All Cells → clean execution (best practice)

✍️ Markdown Cells (Very Important Skill)
Used for:
Notes
Explanations
Reports
Submitting assignments

Example Markdown Cell:
## Data Cleaning Step
- Removed null values
- Normalized columns


Markdown ≠ Python
It never executes.
'''


# 📦 Importing Libraries in Cells
'''
Best practice:

Top cell only
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Don’t scatter imports randomly (common beginner mistake).

📊 Visualization (Why Cells Are Loved)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y)
plt.show()


📌 Output appears right below the cell

No terminal. No pop-up window.
'''



# 🔄 Re-running Cells (Live Experimentation)

'''
change only one line:

y = [10, 40, 90, 160]


Re-run → graph updates instantly
This is why notebooks dominate ML & data science

🧪 Debugging with Cells

Instead of:

print(a)
print(b)
print(c)


You just write:

a
b
c


Cleaner. Faster. Smarter.

🧠 Advanced Cell Concepts (Now We Level Up 🔥)
1️⃣ Magic Commands (Cell Superpowers)

These start with % or %%

Line magic
%time sum(range(1000000))

Cell magic
%%time
total = 0
for i in range(1000000):
    total += i


2️⃣ Running Shell Commands
!pip install numpy
!ls
!pwd


Notebook can talk to OS directly.

3️⃣ Multiple Outputs Per Cell
a = 5
b = 10
a
b


Output:

5
10


Normal Python can’t do this.

4️⃣ Stateful Execution (Danger + Power)
counter = 0


Run this cell 5 times:

counter += 1
counter


You get:

1 → 2 → 3 → 4 → 5


Same code, different result 😈
This is power and risk.

🏗️ Professional Notebook Structure
A clean notebook looks like:
Title + Objective (Markdown)

Imports
Data loading
Cleaning
Processing
Visualization
Conclusion

This is how:
PES University expects
Companies expect
Projects get marks
'''


# 🆚 Notebook vs .py Script
'''
Feature	Notebook	.py file
Interactive	✅	❌
Visualization	Excellent	Average
Debugging	Easy	Medium
Production	❌	✅
Learning	🔥🔥🔥	❌
🎯 When to Use Cell Scripts

Use notebooks for:
Learning
ML / AI
Data analysis
Research
Assignments
Interviews (demos)

Use .py for:
Apps
APIs
Automation
Deployment
'''