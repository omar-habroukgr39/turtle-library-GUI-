from turtle import *
import math
import random

s = Screen()
s.bgcolor("black")

# Setup border
my_pen = Turtle()
my_pen.color("white")
my_pen.speed(10)
my_pen.penup()
my_pen.goto(-300, -300)
my_pen.pendown()
my_pen.pensize(3)

for _ in range(4):
    my_pen.fd(600)
    my_pen.lt(90)

player = Turtle()
player.penup()
player.shape("turtle")
player.color("red")
player.speed(0)
player.shapesize(3)


ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.speed(0)
ball.setpos(-100, -100)

speedo = 1
score_counter = 0

# Score display
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-400, 290)
score_display.write(f"Score: {score_counter}", align="left", font=("Arial", 16, "normal"))


def turn_left():
    player.lt(15)


def turn_right():
    player.rt(15)


def turn_down():
    global speedo
    speedo -= 1
    if speedo < 1:
        speedo = 1


def turn_up():
    global speedo
    speedo += 1


def move():

    player.fd(speedo)
    s.ontimer(move, 20)
    # Check boundaries
    if player.xcor() > 260 or player.xcor() < -260 or player.ycor() > 260 or player.ycor() < -260:
        player.lt(180)

    distances = math.dist((player.xcor(), player.ycor()), (ball.xcor(), ball.ycor()))
    if distances < 40:
        global score_counter
        ball.setpos(random.randint(-290, 290), random.randint(-290, 290))
        score_counter += 1
        update_score()

def move_ball():
    ball.fd(3)
    s.ontimer(move_ball, 20)

    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.lt(180)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.lt(180)


def update_score():
    score_display.clear()
    score_display.write(f"Score: {score_counter}", align="left", font=("Arial", 16, "normal"))

s.listen()
s.onkeypress(turn_left, 'Left')
s.onkeypress(turn_right, 'Right')
s.onkeypress(turn_up, 'Up')
s.onkeypress(turn_down, 'Down')

move()
move_ball()
my_pen.hideturtle()
mainloop()


