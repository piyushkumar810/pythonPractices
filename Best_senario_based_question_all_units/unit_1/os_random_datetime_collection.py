
# --------------------------- working with os
import os
print(os.name)
print(os.getpid())
print(os.getppid())

path1=r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\Best_senario_based_question_all_units\unit_1\haaaaaaa.txt"
path2=r"rut//time//html.txt"

full_path=os.path.join(path1,path2)
print(full_path)
# print(os.listdir(path1))

# print(os.mkdir(path1))
# print(os.rmdir(path1))


# -------------------------------- working with random module
import random

# random.seed(5)
print(random.randint(1, 10))
print(random.randint(1, 10))

a = [1,2,3,4,5,6,7,7,8,9]

print(random.choice(a))


random.shuffle(a)
print(a)

print(random.randrange(7,18))



# -------------------------------- datetime
from datetime import date,time,datetime,timedelta

current_date=datetime.now()
print(current_date)

d = date(2026, 2, 4)
t = time(10, 30, 45)
dt = datetime(2026, 2, 4, 10, 30, 45)

print(d)
print(t)
print(dt)
