'''
🧠 Scenario-Based Question: Composition (HAS-A Relationship)
📌 Scenario
You are developing a Car Management System.
A Car is made up of several components:
An Engine
A FuelTank

These components:
Exist as independent classes
Are used by Car
Must be created inside the Car class

📝 What YOU have to do
1️⃣ Create a class Engine
Attribute: engine_type
Method: start_engine() → prints engine started message

2️⃣ Create a class FuelTank
Attribute: capacity
Method: show_capacity() → prints fuel tank capacity

3️⃣ Create a class Car
Attribute: model
Car HAS an Engine
Car HAS a FuelTank

4️⃣ Rules (VERY IMPORTANT)
Use composition, not inheritance
Create Engine and FuelTank objects inside Car
Access component methods through Car
Do NOT use global objects

5️⃣ Object creation & usage
Create one Car object
Call:
Engine start
Fuel tank capacity display

❌ Do not use inheritance
❌ Do not merge classes
✔ Follow HAS-A relationship strictly
'''

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        print(f"{self.engine_type} engine started")


class FuelTank:
    def __init__(self, capacity):
        self.capacity = capacity

    def show_capacity(self):
        print(f"Fuel tank capacity: {self.capacity} liters")


class Car:
    def __init__(self, model, engine_type, fuel_capacity):
        self.model = model
        self.engine = Engine(engine_type)       # Car HAS an Engine
        self.fuel_tank = FuelTank(fuel_capacity) # Car HAS a FuelTank

    def start_car(self):
        print(f"Car model: {self.model}")
        self.engine.start_engine()

    def show_fuel_info(self):
        self.fuel_tank.show_capacity()

car1 = Car("Tesla Model X", "Electric", 80)

car1.start_car()
car1.show_fuel_info()
