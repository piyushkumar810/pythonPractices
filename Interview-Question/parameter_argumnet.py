# ---------------- difference between parameter and argument

# The terms parameter and argument are often used interchangeably, but they have distinct meanings in the context of functions in programming:

# Parameter
'''A parameter is a variable in a function definition. It acts as a placeholder for the value that will be provided when the function is called.
Parameters specify what kind of input a function can accept.'''

# Argument
'''An argument is the actual value or data passed to a function when you call it. It is the value assigned to a function’s parameter.
Arguments provide the specific data that the function will work with during a particular call.
Example:'''


def greet(name):  # `name` is a parameter
    print(f"Hello, {name}")
greet("Alice")  # "Alice" is an argument

# In this example, name is a parameter of the greet function. It represents a value that the function expects to receive when called.