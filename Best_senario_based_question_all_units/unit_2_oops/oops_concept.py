'''
9️⃣ Modifying Attribute Values (3 Ways)
🔸 Way 1: Directly through object
laptop.battery_level = 85


✔ Simple
❌ No validation (dangerous)

🔸 Way 2: Using a method (BEST PRACTICE)
def update_battery_level(self, new_level):
    if 0 <= new_level <= 100:
        self.battery_level = new_level


✔ Controlled
✔ Safe
✔ Encapsulation respected

🔸 Way 3: Increment / Decrement using method
def decrease_battery(self, usage):
    self.battery_level -= usage


✔ Real-world modeling
✔ Logic + data together
'''