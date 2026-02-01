#---------------------------------- Dangerous because most of one don't know
#                                 UNIT–1 THEORY – COMPLETE ANSWERS (PESU READY)

# 1️⃣ Python Execution Model
# Question:
# Explain the execution model of Python.
'''
Answer:

Python follows an interpreted execution model with bytecode compilation.
The Python source code (.py) is first converted into an intermediate form called bytecode (.pyc). 
This bytecode is then executed by the Python Virtual Machine (PVM).

Unlike compiled languages, Python does not directly generate machine code. 
The execution happens line by line through the interpreter.
'''

# 2️⃣ Scope of Variables
# Question:
# Explain the scope of variables in Python.
'''
Answer:

The scope of a variable determines where it can be accessed in a program.
Python supports four types of scope:
Local - variables defined inside a function
Global - variables defined outside all functions
Enclosing (nonlocal) -variables in outer functions

Built-in -predefined names like print, len

Python follows the LEGB rule to resolve variable scope.'''


# 3️⃣ Mutable vs Immutable Data Types
# Question:
# Differentiate between mutable and immutable data types.

# Answer:
# Mutable	                               Immutable
# Can be changed after creation	           Cannot be changed
# Example: list, set, dictionary	        Example: int, float, string, tuple
# Memory location remains same	            New object is created

# Strings are immutable because modifying them creates a new object instead of changing the existing one.


# 4️⃣ Parameters vs Arguments
# Question:
# Differentiate between parameters and arguments.
'''
Answer:
Parameters are variables defined in a function definition.
Arguments are values passed to the function during function call.

Example:

def add(a, b):   # a, b → parameters
    return a + b

add(2, 3)       # 2, 3 → arguments
'''

# 5️⃣ Return Statement vs Print
# Question:
# Differentiate between return and print statements.
'''
Answer:
return	print
Sends value back to caller	Displays output on screen
Ends function execution	Does not end function
Can be stored in variable	Cannot be stored

A function without a return statement returns None.
'''

# 6️⃣ Comprehensions
# Question:
# What are comprehensions in Python?
'''
Answer:

Comprehensions provide a concise way to create collections using a single line of code.

Types of comprehensions:
List comprehension
Set comprehension
Dictionary comprehension

Python does not support tuple comprehension; it creates a generator instead.

Comprehensions are faster and more readable than traditional loops.
'''

# 7️⃣ Iterables vs Iterators
# Question:
# Differentiate between iterable and iterator.
'''
Answer:
Iterable	                       Iterator
-------------------------------------------------------------------
Can be looped over	               Produces values one at a time
Example: list, tuple	           Example: iter(list)
Uses __iter__()	                   Uses __next__()

Iterators raise a StopIteration exception when elements are exhausted.
'''

# 8️⃣ Decorators
# Question:
# What is a decorator in Python?
'''
Answer:

A decorator is a function that modifies the behavior of another function without changing its source code.
Decorators are used for logging, authentication, timing, and access control.

They are implemented using the @ symbol.
'''

# 9️⃣ Python Standard Library
# Question:
# Explain the Python Standard Library.
'''
Answer:

The Python Standard Library is a collection of built-in modules that provide predefined functionalities such as file handling, date and time operations, system-level tasks, and data manipulation.

Examples:
os - operating system interaction
sys - system-specific parameters
datetime - date and time operations
collections - advanced data structures
'''

# 🔟 Advantages of Python
# Question:
# List advantages of Python.
'''
Answer:

Easy to learn and use
Interpreted and high-level language
Platform independent
Large standard library
Supports multiple programming paradigms
Dynamic typing and automatic memory management
'''