# ------------------------------practical use case of decorater in python

import logging

def log_function_call(func):
    def decorater(*args,**kwargs):
        logging.info(f"calling {func.__name__} with agrs={args} , and kwargs={kwargs} ")
        result=func(*args,**kwargs)
        logging.info(f"{func.__name__} returned {result} ")
        return result
    return decorater

@log_function_call
def my_function(a,b): 
    return a+b

my_function(1,3)