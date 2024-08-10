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
