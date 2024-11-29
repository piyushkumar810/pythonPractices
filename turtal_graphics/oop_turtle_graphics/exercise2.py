# draw every shape connected to each other (triangle,rectangle,pentagon,hep hex,oct,none,dec ..)

from turtle import Turtle,Screen
s1=Screen()
t1=Turtle()

for i in range(3,11):
    # pick this color from tk color combination
    col=["black", "red", "green", "yellow", "orange", "pink", "blue", "gray", "white","red"]
    n=360/i
    # print(n)

    j=1
    while(j<=i):
        t1.color(col[i-3])
        t1.forward(100)
        t1.left(n)

        j+=1

    i+=1

s1.exitonclick()