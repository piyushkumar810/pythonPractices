# ------------------------------learning some built in methods in python

a="PiyUsh KumAr"

# 1st --> len()
print(len(a))

# 2nd -->upper()
print(a.upper())

# 3rd -->lower()
print(a.lower())

# 4th -->rstrip():- used to remove trailing character, it will not remove leading trailing character
b="!!!! piyush !!!!!!!"
print(b)
print(b.rstrip("!"))

# 5th -->replace()
print(b.replace("piyush","harry"))

# 6th -->split():- this method is used to split the string into a list, you can use separator also
c="i will study python daily"
print(c)
print(c.split(" "))

# 7th -->capitalize():- only 1st character of string ko captial kar dega
print(c.capitalize())

# 8th -->title():- it will capitalize every word 1st letter
print(c.title())

# 9th -->center()
print(c)
print(c.center(50))
print(len(c.center(50)))

# 10th -->count():- count the specified word occured in that string
d="you have to learn python you have no other option"
print(d.count("you"))

# 11th -->find()/index()
print(d.find("you"))

# 12th -->startswith()/endswith()
print(d.endswith("option"))

# 13th -->isalphanum()
e="HiPiyushYouMobNoIs8102356837"
print(e.isalnum())

# 14th -->isalpha()
print(e.isalpha())
f="HiPiyush"
print(f.isalpha())

# 15th -->islower()/isupper()
print(f.islower())
print(f.isupper())

# 16th -->isprinted():- if any non printable character(\n , \t , " ") is their in the string then it will return false.
g="hi piyush \n you strated python"
print(g.isprintable())
print(f.isprintable())

# 17th -->swapcase()
h="piyush"
i="PIYUSH"
j="PiYuSh"
print(h.swapcase())
print(i.swapcase())
print(j.swapcase())