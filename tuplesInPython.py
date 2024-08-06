# -------------------------tuples in python
country=("india","russia","china","america","germainy","japan","saudi","koria")
print(len(country))
print(type(country),country)
mixture=(1,34,68,"piyush",True)
print(mixture)

# checking which is tuple and which is not
name=("piyush")
print(type(name))
name1=("piyush",)
print(type(name1))
print("\n")

# basic difference between list and tuple :- list is mutable but tuple is immutable
name3=["hello","hi"]
name3.append("bye")
print(name3)
print("\n")

# you cannot directly change in tuple because tuple are immutable 1st you have to change it to list then do modification and then agian change it to tuple
name4=("hello", "piyush")
# name4.append("bye")
temp=list(name4)
temp.append("bye")
temp[0]="roll 28"
name4=tuple(temp)
print(name4)