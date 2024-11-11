# ------------------------------------- Types of error ------------------------------------

# In Python, errors can be classified into several types. These errors occur when the Python interpreter encounters a problem in the code. Here are the main types of errors in Python:

# 1. Syntax Errors
'''These errors occur when Python can't parse your code because it doesn't follow the correct syntax 
rules of the language.'''

# Example:

# print("Hello world"
# This will raise a SyntaxError because the closing parenthesis ) is missing.

# SyntaxError: unexpected EOF while parsing



# 2. Runtime Errors (Exceptions)
'''These errors occur while the program is running, after the code is syntactically correct. 
They happen when the program tries to perform an operation that isn't allowed or doesn't make sense.'''

# Common Runtime Errors:
# ZeroDivisionError: Occurs when dividing a number by zero.

# x = 5 / 0

# ZeroDivisionError: division by zero
'''IndexError: Occurs when trying to access an index that is out of range in a list or other indexed collection.

python
Copy code
my_list = [1, 2, 3]
print(my_list[5])
Message:

sql
Copy code
IndexError: list index out of range
ValueError: Occurs when a function receives an argument of the right type, but an inappropriate value.

python
Copy code
int("hello")
Message:

csharp
Copy code
ValueError: invalid literal for int() with base 10: 'hello'
TypeError: Occurs when an operation or function is applied to an object of inappropriate type.

python
Copy code
"hello" + 5
Message:

python
Copy code
TypeError: can only concatenate str (not "int") to str
KeyError: Raised when trying to access a key that does not exist in a dictionary.

python
Copy code
my_dict = {"name": "John"}
print(my_dict["age"])
Message:

vbnet
Copy code
KeyError: 'age'
3. Logical Errors
Logical errors occur when the program runs without crashing, but it doesn't do what you expect because of a flaw in the logic of your code. These are usually harder to detect because there are no error messages.

Example:
python
Copy code
x = 10
y = 5
result = x - y  # You expected multiplication, but used subtraction
print(result)  # Output: 5, not 50
4. Indentation Errors
Python relies on indentation to define code blocks. If the indentation is inconsistent, an IndentationError occurs.

Example:

python
Copy code
def greet():
print("Hello!")  # This line should be indented
Message:

makefile
Copy code
IndentationError: expected an indented block
5. Import Errors
These occur when Python cannot find the module you're trying to import.

Example:

python
Copy code
import non_existent_module
Message:

vbnet
Copy code
ModuleNotFoundError: No module named 'non_existent_module'
6. Name Errors
A NameError occurs when Python encounters a variable or function name that it doesn't recognize (i.e., it's not defined or not in scope).

Example:

python
Copy code
print(x)
Message:

csharp
Copy code
NameError: name 'x' is not defined
7. File Errors
These errors occur when there are issues with file handling, such as trying to open a file that doesn’t exist.

Example:

python
Copy code
with open("non_existent_file.txt", "r") as f:
    content = f.read()
Message:

vbnet
Copy code
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
8. AssertionError
This error is raised when an assert statement fails. The assert keyword is used for debugging purposes, and it tests if a condition is true. If it's false, an AssertionError is raised.

Example:

python
Copy code
assert 2 + 2 == 5  # This will fail
Message:

php
Copy code
AssertionError
9. OverflowError
Occurs when a number is too large to be represented.

Example:

python
Copy code
import sys
sys.setrecursionlimit(10000)  # A recursion limit can be too high
Message:

makefile
Copy code
RecursionError: maximum recursion depth exceeded
10. MemoryError
Occurs when the system runs out of memory (RAM) during the execution of the program.

Example:

python
Copy code
a = [1] * (10**10)  # Trying to create a very large list
Message:

Copy code
MemoryError'''