# -------------------------- arithematic operatin in numpy arrray(lec-07)

# a+b      -->  np.add(a,b)
# a-b      -->  np.subtract(a,b)
# a*b      -->  np.multiply(a,b)
# a/b      -->  np.divide(a,b)
# a%b      -->  np.mod(a,b)
# a**b     -->  np.power(a,b)
# 1/a      -->  np.reciprocal(a,b)


import numpy as np
# ---------------------------addition
var1=np.array([1,2,3,4,5])
var2=np.array([6,7,8,9,5])
sum=np.add(var1,var2)
# sum=var1+var2
print(sum)
print("\n")


# ------------------------- substract
varS1=np.array([1,2,3,4,5])
varS2=np.array([6,7,8,9,5])
sub=np.subtract(varS1,varS2)
# sub=varS2-varS1
print(sub)
print("\n")

# ------------------------- multiply
varM1=np.array([1,2,3,4,5])
varM2=np.array([6,7,8,9,5])
mul=np.multiply(varM1,varM2)
print(mul)
print("\n")

# -------------------------- divide
varD1=np.array([1,2,3,4,5])
varD2=np.array([6,7,8,9,5])
div=np.divide(varD1,varD2)
print(div)
print("\n")

# -------------------------- modulo division
varMD1=np.array([1,2,3,4,5])
varMD2=np.array([6,7,8,9,5])
Mdiv=np.mod(varMD1,varMD2)
print(Mdiv)
print("\n")

# -------------------------- power
varP1=np.array([1,2,3,4,5])
varP2=np.array([6,7,8,9,5])
pow=np.pow(varP1,varP2)
print(pow)
print("\n")

# -------------------------- reciprocal
varRep=np.array([3,6,1,8])
repArr=np.reciprocal(varRep)
print(repArr)
print("\n")

#---------------- working with 2-d array
var2d=np.array([[2,5,7],[5,8,9]])
var2da=np.array([[4,5,7],[6,1,2]])
sum=np.add(var2d,var2da)
# sum=var2d+var2da
print(var2d)
print()
print(var2da)
print()
print(sum)