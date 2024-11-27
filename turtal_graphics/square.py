import turtle

# 1st program making square

turtle.getscreen()  # used to get the screen

# if you want to change the shape of the arrow which lies on the middle of the output screen
## turtle.shape("turtle")
# threr is only 6 shape (arrow, turtle, circle, square, triangle, classic)

# to find which shape you are using
print(turtle.shape())



turtle.forward(100) # this 100 is in pixels (forward and backword works on pixels)
turtle.left(90)     # this 90 is in degree  (left and right works on degree)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()# this is used to hold the screen unless you click on screen