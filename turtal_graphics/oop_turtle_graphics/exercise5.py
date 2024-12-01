# ----------------------------circle

import random
import turtle
from turtle import Turtle,Screen
S1=Screen()
t1=Turtle()
t1.speed("fast")
turtle.colormode(255)

# checking heading of the circle because we have to stop there
t1.heading()

while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    t1.pencolor(r,g,b)
    t1.circle(100)
    # 
    t1.left(8)

    if t1.heading()==0:
        break


S1.exitonclick()