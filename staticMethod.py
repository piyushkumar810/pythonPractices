# --------------------------Static method in pyhton

class math:
    def __init__(self,num):
        self.num=num

    def addToNum(self, n):
        self.num=self.num + n

    @staticmethod
    def add(a,b):
        return a+b

a=math(6)
print(a.num)

a.addToNum(5)
print(a.num)

# print(math.add(2,9))
c=math.add(2,8)
print(c)
