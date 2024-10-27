# --------------------------Encapsulation in python 

# wrraping of data and method into single unit

class person:
    def __init__(self,name,age):
        self._name=name
        self.__age=age

    def get_data(self):
        return self.__age

    def set_data(self,age):
        if age>0:
            self.__age=age
        else:
            print("p;ease enter valid age")

    def display(self):
        print(f'name={self._name} , age={self.__age}')

p=person("piyush", 18)
print(p.get_data())

p.set_data(30)
p.display()