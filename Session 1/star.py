from turtle import *

star = Turtle()

screen = Screen()

screen.bgcolor("black")

star.color("purple")

size = 500

for i in range(5):
    star.pensize(5)
    star.forward(size)
    star.right(144)


star.hideturtle()


done()
