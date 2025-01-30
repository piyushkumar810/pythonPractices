# ----------------------------- statical function---------------------------------

import numpy as np
baked_food=[200,300,150,130,200,280,170,188]

a=np.array(baked_food)
print(a)
print()
print(np.mean(a)) # sum of all the values/ no of values
print()
print(np.median(a)) # to find median 1st arrange  the no's in ascending order then apply median formula
print()


# if you want to find mode then numpy has no mode function you have to import another liberary that is statistics
import statistics as st
print(st.mode(a)) # most occuring value
print()

# std stands for standered devation
print(np.std(a))
print()

# var stands for variance
print(np.var(a)) 



# ----------------------------------- correlation coefficient-----------------------
# correlation cofficient value lies between -1 to 1
# where, 
#  -1 = represent inversely porportional relationship
#  1 = represent proportional relationship
#  0 = means no relationship

# example 1:- 
tabacco_consumption=[30,50,10,30,50,40]
deaths=[100,120,70,100,120,112]

print(np.corrcoef([tabacco_consumption,deaths]))
print()

# example 2:- 
price=[300,100,350,150,200]
sales=[10,20,7,17,3]
print(np.corrcoef([price,sales]))
# prices increase kar rha hai tho sales decrease ho rha hai and sales increase ho rha hai tho price decrease ho rha hai