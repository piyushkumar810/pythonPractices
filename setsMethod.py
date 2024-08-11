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