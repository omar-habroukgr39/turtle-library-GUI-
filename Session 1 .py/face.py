import turtle
from turtle import *

root = Turtle()


# Draw large circle
root.penup()
root.goto(0, -200)
root.pendown()
root.circle(200)

# Draw left eye
root.penup()
root.goto(-80, 20)
root.pendown()
root.circle(50)

# Fill left eye
root.color("black")
root.begin_fill()
root.circle(25)
root.end_fill()

# Draw right eye
root.penup()
root.goto(80, 20)
root.pendown()
root.circle(50)

# Fill right eye
root.begin_fill()
root.circle(25)
root.end_fill()

# Draw lips
root.penup()
root.goto(5, -130)
root.pendown()
root.color("red")
root.begin_fill()
root.circle(40)
root.end_fill()

done()