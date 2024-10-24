# ---------------------------------diamond problem

# in python the diamond problem can be easily resolved by using mro() 'method resolution order' 

# ----------------what does mro() do
# ans --> it is used to get the order in which the method and attribute are to be inhertied from hierarchie
# of the classes(thos problem specially arrise in case of multiple inheritance)

# eg

class a:
    def display(self):
        print("display method from a class")

class b(a):
    def display(self):
        print("display method from b class")

class c(a):
    def show(self):
        print('hi from c class')

class d(b,c):
    pass

obj_d=d()
obj_d.display()

# how does this work (obj_d printed b class object)
# ans --> this happens with the help of mro()
# the algorithm used inside mro() ============== c3 linearization