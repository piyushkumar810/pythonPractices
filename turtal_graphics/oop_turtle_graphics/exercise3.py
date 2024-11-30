# random walk with random color

import turtle
from turtle import Turtle,Screen
import random
t1=Turtle()
s1=Screen()
t1.speed("fastest")
t1.width(10)
# t1.shape("turtle")
# col=["black", "red", "green","azure2","blanchedalmond","cadetblue1", "yellow", "orange", "aqua","pink", "blue", "gray","aquamarine3", "antiquewhite3"]
turtle.colormode(255)

for _ in range(100):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    t1.setheading(random.randrange(0,360,90))  # it will generate randomly 0 - 360 degree randomly with the gap of 90 degree
    # setheading is a turtle method which have diractions (0-east, 90-north, 180-west, 270-south)

    # t1.pencolor(random.choice(col))
    t1.pencolor((r,g,b))
    t1.forward(30)
    

s1.exitonclick()