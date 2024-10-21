# add to complex number

# class addComplex:
#     def __init__(self,real,imagionary):
#         self.r=real
#         self.i=imagionary

#     def __add__(self,x):
#         return f"{self.r + x.r} + {self.i + x.i}i "

# c1=addComplex(4,7)
# c2=addComplex(3,6)

# print(c1+c2)


class addComplex:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __add__(self, x):
        return addComplex(self.r + x.r, self.i + x.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = addComplex(4, 7)
c2 = addComplex(3, 6)
c3 = addComplex(5, 2)

# Adding multiple complex numbers
result = c1 + c2 + c3

print(result)