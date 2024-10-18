from emp2 import employee
e=employee("piyush")
print(e)

# -----------what does __str__() and __repr__() method do
# the str and repr method are both used to convert object to string representation, but the main difference 
# between repr and str is if python did'nt find __str__() method and if __repr__() is present then pyhton 
# will fallback to __repr__()