'''
🧠 Scenario-Based Question (Methods + Attributes)
📌 Scenario
You are building a Mobile Phone Battery Management System.
Each mobile phone should:
Store brand, model, and battery_level
Battery level should start at 100 by default

Allow the user to:
Check battery level
Use the phone, which reduces battery
Charge the phone, which increases battery

Battery level:
Must never go below 0
Must never exceed 100

📝 Your Task (WRITE CODE)
Requirements:
Create a class Mobile
Attributes:
brand
model
battery_level (default = 100)

Methods:
check_battery() → prints battery percentage

use_phone(usage)
reduces battery by usage
if usage is more than available battery → set battery to 0

charge_phone(amount)
increases battery by amount
if battery exceeds 100 → set to 100


🔍 Sample Usage (Expected Behavior)
m1 = Mobile("Samsung", "S23")

m1.check_battery()      # 100%
m1.use_phone(30)
m1.check_battery()      # 70%
m1.charge_phone(50)
m1.check_battery()      # 100%
m1.use_phone(150)
m1.check_battery()      # 0%
'''


# ---------------------------------- solution
class Mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.battry_level=100

    def check_battery(self):
        print(f"{self.battry_level}%")

    def use_phone(self,usage):
        self.usage=usage
        self.battry_level=self.battry_level-self.usage

        if(self.usage>self.battry_level):
            self.battry_level=0

    def charge_phone(self,amount):
        self.amount=amount
        self.battry_level=self.battry_level+self.amount

        if(self.battry_level>100):
            self.battry_level=100

mob=Mobile("Apple","iphone_17ProMax")
mob.check_battery()
mob.use_phone(30)
mob.check_battery()
mob.charge_phone(50)
mob.check_battery()


# previous code is correct but wrote like a child
# see how to write

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery_level = 100

    def check_battery(self):
        print(f"{self.battery_level}%")

    def use_phone(self, usage):
        if usage < 0:
            print("Usage cannot be negative")
        elif usage >= self.battery_level:
            self.battery_level = 0
        else:
            self.battery_level -= usage

    def charge_phone(self, amount):
        if amount < 0:
            print("Charge amount cannot be negative")
        elif self.battery_level + amount > 100:
            self.battery_level = 100
        else:
            self.battery_level += amount

mob1=Mobile("Apple","iphone_17ProMax")
mob1.check_battery()
mob1.use_phone(30)
mob1.check_battery()
mob1.charge_phone(50)
mob1.check_battery()
