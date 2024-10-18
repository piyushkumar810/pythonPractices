# ----------------------------method overriding in pyhton

# it occures when a sub class provide a specific implementation for a mehtod that is already defined in its super class

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14*super().area()
    
rectangle=shape(3,5)
print(rectangle.area())

cir=circle(5)
print(cir.area())