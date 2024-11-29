# Q) draw a dashed 100px line 

from turtle import Turtle,Screen
s1=Screen()
t=Turtle()

for _ in range(10):
    t.color("red")
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

s1.exitonclick()