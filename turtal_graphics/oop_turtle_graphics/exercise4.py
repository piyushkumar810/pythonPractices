# --------------------turtle star in python-----------------------

from turtle import  Turtle,Screen
s1=Screen()
t1=Turtle()

t1.color("red","yellow")

# why we need this heading/position ?
# ans--> because we need to stop the arrow so, we stored heading of arrow and at same place when it will
#          reach again there then it will stop drawing.

t1.heading()
# direction_of_arrow=t1.heading()
# print(direction_of_arrow)
# -----------------------or 
# position_of_arrow=t1.position()
# print(position_of_arrow)

t1.begin_fill()
while True:
    t1.forward(200)
    t1.left(170)

    if t1.heading()==0:
        break

t1.end_fill()

s1.exitonclick()