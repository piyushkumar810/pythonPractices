# ------------------------------------- datetime module in python

import datetime as dt

# it will give you current live date with time and even second
current_date=dt.datetime.now()
print("current date = ",current_date)
print()


# if you want to know that the year (1997/10/14) which day this year is of
# strftime() function will help you to get these following details:- 

know_day=dt.datetime(1997,10,14)
print(know_day)
print()
# %A = will help you to know which day it is 
print(know_day.strftime("%A"))
print()

# %a = it will give you same day name in sort form 
print(know_day.strftime("%a"))
print()

# %B = will help you to know which month name it is 
print(know_day.strftime("%B"))
print()

# %m = will help you to know which month number it is 
print(know_day.strftime("%m"))
print()

# %Y = will help you to know which year it is 
print(know_day.strftime("%Y"))
print()

# %p = for am/pm
print(know_day.strftime("%p"))
print()

# %S = for second
print(know_day.strftime("%S"))