class Distance:
    count = 0   # class variable

    def __init__(self):
        self.km = 0
        self.m = 0
        Distance.count += 1

    def get_distance(self):
        self.km = int(input("Enter kilometers: "))
        self.m = int(input("Enter meters: "))

    def add_distance(self, other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        total_km += total_m // 1000
        total_m = total_m % 1000

        result = Distance()
        result.km = total_km
        result.m = total_m
        return result

    def show_distance(self):
        print(f"{self.km} kms {self.m} mts")


# Client code
d1 = Distance()
d1.get_distance()

d2 = Distance()
d2.get_distance()

d3 = d1.add_distance(d2)

print("First Distance:")
d1.show_distance()

print("Second Distance:")
d2.show_distance()

print("Total Distance:")
d3.show_distance()

print("Total Distance objects created:", Distance.count)

