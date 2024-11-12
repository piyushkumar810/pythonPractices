class change:
    def __init__(self,x,y,z):
        self.a=x+y+z
    
x=change(1,2,3)
y=getattr(x,'a')
setattr(x,'a',chr(y+59))
print(x.a)

# what is getattr and setattr

''' In Python, getattr and setattr are built-in functions that allow you to interact with an object's
  attributes dynamically. Here’s a breakdown of what each function does:'''

# 1. getattr
'''The getattr function is used to retrieve the value of an attribute from an object. It takes two or three
   arguments:'''
# Syntax: getattr(object, attribute_name[, default])

'''object: The object you want to get the attribute from.
   attribute_name: The name of the attribute (as a string) you want to retrieve.
   default (optional): A value to return if the attribute does not exist. If not 
                       provided and the attribute doesn’t exist, it raises an AttributeError.'''

# 2. setattr
'''The setattr function is used to set or update the value of an attribute on an object. It takes three
    arguments:'''
# Syntax: setattr(object, attribute_name, value)

'''object: The object on which you want to set the attribute.
   attribute_name: The name of the attribute (as a string) you want to set.
   value: The value to assign to the attribute.'''