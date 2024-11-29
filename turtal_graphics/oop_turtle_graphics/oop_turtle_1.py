from turtle import Turtle, Screen # importing turtle class
t=Turtle() # creating object of turtle class
s1=Screen()

t.color("red")
t.circle(100)
t.penup()
print(t.isdown()) # it will check is your pen is down or not
t.right(90)
t.forward(50)
t.pendown()
print(t.isdown())

t.color("blue","red")

t.begin_fill()
t.pensize(5)    # increase the size of the pen
t.hideturtle()  # it is used to hide the turtle
print(t.isvisible())
t.circle(50)
t.end_fill()

# i want to move the turtle n any specific position
# 1st i want to know the position of my turtle
print(t.position())
t.goto(-50,-50)
t.showturtle()

s1.mainloop()
