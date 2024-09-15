# ------------------------------Getter and setter in pyhton
class myclass:
    def __init__(self, value):
        self._value=value
    
    @property
    def value(self):
        return self._value
    
a=myclass(10)
print(a.value)

# setter --> it is important to note that getter do not take any parameter and we cannot set value through getter for that we need setter which can be added by  decorater method with @property_name.setter