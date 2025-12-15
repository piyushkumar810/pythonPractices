'''
You are developing a Car Rental System in Python using the MVC (Model-View-Controller) architecture.

car_rental_system/
│
├── model/
│   └── car.py
│
├── controller/
│   └── booking_controller.py
│
├── view/
│   └── user_view.py
│
└── main.py


The following import statement is written in main.py:
--from model.car import Car

When executing main.py, the following error occurs:
--ModuleNotFoundError: No module named 'model'

-------------- why this error is comming ----------------------

'''

# ------------------solution------------------------
'''
Answer the following:

1. Explain why this error occurs.
sol->
1️⃣ Reason for the Error

The error occurs because Python does not recognize the model directory as a package.
In Python:
A file is considered a module
A directory is considered a package only if it contains an __init__.py file
Since the model directory does not contain __init__.py, Python cannot locate the module model.car, resulting in a ModuleNotFoundError.


2. Explain the role of __init__.py in Python packages.
sol->
2️⃣ Role of __init__.py

The file __init__.py serves the following purposes:
It marks a directory as a Python package
It allows modules inside the directory to be imported
It enables hierarchical imports such as:


3. Show how to fix the error with proper justification.
sol->
3️⃣ Fixing the Error

To resolve the error, an empty __init__.py file must be added to all package directories.

car_rental_system/
│
├── model/
│   ├── __init__.py
│   └── car.py
│
├── controller/
│   ├── __init__.py
│   └── booking_controller.py
│
├── view/
│   ├── __init__.py
│   └── user_view.py
│
└── main.py

'''