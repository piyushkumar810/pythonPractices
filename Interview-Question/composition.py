# ---------------------------composition in python

'''In object-oriented programming (OOP), composition is a design principle where one class contains
   instances of other classes as part of its attributes, allowing objects to be built using other objects.
   This is often described as a "has-a" relationship.'''

# For example:

# A Car has an Engine.
# A House has Rooms.

'''In Python, composition is achieved by including one class as an attribute of another class.
    This promotes modularity and code reuse.'''

# Example of Composition in Python:

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting.")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Engine is a part of the Car

    def drive(self):
        print(f"Driving the {self.make} {self.model}.")
        self.engine.start()  # Using the Engine class's method

# Creating an Engine instance
engine = Engine(300)

# Creating a Car instance with the Engine
car = Car("Toyota", "Supra", engine)

# Using the Car's methods
car.drive()