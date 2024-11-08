# ------------------------------match case in python

class revesion:
    def matchcase(self,x):
        match x:
            case 0:
                print(" x is zero")

            case 1:
                print("x is one")

            case 2:
                print("x is two")

            case 4:
                print("x is four")

            case 10:
                print("x is ten")

            case _ if x!=90:
                print("x is not 90")

            case _:
                print(x)


mat=revesion()
x=int(input("Enter the  value of  x : "))
mat.matchcase(x)