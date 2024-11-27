import turtle
turtle.getscreen()
t=turtle.Turtle()
t.speed(1)
# speed--> in tuurtle graphics an integer in the range 0 - 10 

# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1


# making pentagon
# Pentagon has 5 sides; each exterior angle is 72° (360° ÷ 5)
t.forward(100)
t.left(72)

t.forward(100)
t.left(72)

t.forward(100)
t.left(72)

t.forward(100)
t.left(72)

t.forward(100)


turtle.done()