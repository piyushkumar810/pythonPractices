# -------------------------hybrid inheritance in python

class A:
    def work(self):
        print('i can  work')

class B(A):
    def sleep(self):
        print('i can sleep whole day')

class C:
    def play(self):
        print("my fevorite game is cricket")

class D(B,C):
    pass

obj_D=D()
obj_D.work()
print(D.mro())