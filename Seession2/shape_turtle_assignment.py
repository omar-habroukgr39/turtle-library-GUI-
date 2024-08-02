from turtle import *
t = Turtle()
s = Screen()

t.color("white")
s.bgcolor("black")

s.title("Hexagon with different turtle shapes")

t.speed(2)


turtle_shapes = ["classic", "circle", "triangle", "square", "arrow", "turtle"]

while True :
    for i in range(6):
        t.shape(turtle_shapes[i])
        t.forward(100)
        t.right(60)

done()
