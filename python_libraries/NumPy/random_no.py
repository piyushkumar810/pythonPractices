# --------------------------------- create numpy array with random number (lec-05)

#  rand() --> the fnction is used to generate a random value between 0 to 1.
#  randn() --> the function used to generate a random value close to zero. this may return positive as well as negative value as well.
#  ranf() --> the function for doing random sampling in numpy. it returns an array of specified shape and fills it with random floats in the half open  interval [0.0, 1.0)
                #  [0.0, 1.0)-->("[" this symbole means 0.0 is included but ")" this symbole means 1.0 will not included).

#  randint() --> the function is used to generate a random number 

import numpy as np

# 1st -- ----------------------------rand()

# for 1-D array
n=np.random.rand(4)
print(n)
print()
# for 2-D array
n1=np.random.rand(3,4)
print(n1)
print("\n")

# 2nd------------------------------- randn()
n2=np.random.randn(4)
print(n2)
print("\n")

# 3rd------------------------------- ranf()
n3=np.random.ranf(4)
print(n3)
print("\n")

# 4th------------------------------- randint()
n4=np.random.randint(4,6,size=3)
print(n4)
print()
n4=np.random.randint(4,9, size=(3,4))
print(n4)


# note:- rand,randn, and randf () will return value between 0-1 but randint() will return value according to us