from turtle import *
import math
import random

s = Screen()
s.bgcolor("orange red")


my_pen = Turtle()
my_pen.speed(10)
my_pen.penup()
my_pen.goto(-300, -300)
my_pen.pendown()

my_pen.pensize(3)
my_pen.color("lawn green")

for i in range(4):
    my_pen.fd(600)
    my_pen.lt(90)


player = Turtle()
player.penup()
player.shape("turtle")
player.color("green")
player.speed(0)
speed = 1
player.shapesize(3)


ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.speed(0)
speedo = 1
ball.setpos(-100, -100)


def turn_left():
    player.lt(15)


def turn_right():
    player.rt(15)


def up():
    global speedo
    speedo += 1


def move():
    player.fd(speedo)
    s.ontimer(move, 20)

    if player.xcor() > 300 or player.xcor() < -300:
        player.lt(180)

    if player.ycor() > -300 or player.ycor() < -300:
        player.lt(180)
    distances = math.dist((player.xcore(), ball.ycor()), (ball.xcore(), ball.ycore()))
    if distances < 20:
        ball.setpos(random.randint(-290, 290), random.randint(-290, 290))


def moveball():
    ball.fd(speedo)
    s.ontimer(moveball, 20)
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.lt(180)
    if ball.ycor() > -290 or ball.ycor() < -290:
        ball.lt(180)


mainloop()
