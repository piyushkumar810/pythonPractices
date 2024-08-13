# -----------------------------------------Sets method in python

cities={"tokyo", "berlin", "delhi", "madrid"}
cities1={"tokyo", "seoul", "kabul", "madrid"}

# 1st --> union
cities2=cities.union(cities1)
print(cities2)

# 2nd --> intersection
cities3=cities.intersection(cities1)
print(cities3)

# 3rd --> intersection_update
cities5=cities.intersection_update(cities1)
print(cities5)

# 4th --> symmetric_difference
cities6=cities.symmetric_difference(cities1)
print(cities6)

# 5th --> difference
cities7=cities.difference(cities1)
print(cities7)

# 6th --> isdisjoint()
print(cities.isdisjoint(cities1))

# 7th --> issuperset()
num={3, 6, 7, 12, True, 49.9}
num2={7, True, 49.9}
print(num.issuperset(num2))

# 8th --> issubset()
print(num2.issubset(num))

# add()
num2.add(77)
print(num2)

# pop()
num2.pop()
print(num2)

# clear()
num2.clear()
print(num2)