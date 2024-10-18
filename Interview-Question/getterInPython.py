# -----------------------------------getters in python

# what is the difference between these two program because both do same work and same output

class myclass:
    def __init__(self,value):
        self._value=value 

    def show(self):
        print(f"the value is {self._value}")

    @property
    def ten_value(self):
        return 10*self._value
    
cls=myclass(10)
cls.show()
print(cls.ten_value)


# class myclass:
#     def __init__(self,value):
#         self._value=value 

#     def show(self):
#         print(f"the value is {self._value}")

#     # @property
#     def ten_value(self):
#         return 10*self._value
    
# cls=myclass(10)
# cls.show()
# print(cls.ten_value())



# -------------------------------------------explanation

# The key difference between the two versions of your program lies in how the ten_value method
#  is accessed: one uses the @property decorator, and the other does not.

# with @property decorator
'''The ten_value method is treated like an attribute. You access it as cls.ten_value without parentheses.'''

'''When using @property, it allows you to create "getter" methods that can be accessed like 
attributes but still function like methods.'''

'''This is useful when you want to encapsulate logic but make the class more intuitive to use, 
appearing as if it's just retrieving a value.'''