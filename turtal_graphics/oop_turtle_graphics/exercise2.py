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

# ----------------------------------------or--------------------------------------------

# import random
# from turtle import Turtle,Screen
# s1=Screen()
# t1=Turtle()

# col=["black", "red", "green","azure2","blanchedalmond","cadetblue1", "yellow", "orange", "aqua","pink", "blue", "gray","aquamarine3", "antiquewhite3"]
# for i in range(3,11):
#     angle=360/i
#     t1.pencolor(random.choice(col))

#     for _ in range(i):
#         t1.forward(100)
#         t1.right(angle)

# s1.exitonclick()