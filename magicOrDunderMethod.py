# ------------------------magic or dunder() method in python

# magic method is defined in class and their purpose is to perform some special task.
# these method starts with double underscore and ends with double underscore.

# eg :- __len__()  ,  __init__()  ,  __str__()  ,  __repr__() ...........etc

# 1st -> __len__()
class employee():
    name="piyush"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
emp=employee()
print(len(emp))