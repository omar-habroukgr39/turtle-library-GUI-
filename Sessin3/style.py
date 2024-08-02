# import turtle as t
#
# # Set up the screen
# screen = t.Screen()
# screen.bgcolor("lightblue")
#
# # Create a turtle for drawing the car
# car = t.Turtle()
# car.color("red")
# car.speed(1)
# car.penup()
#
# # Draw the body of the car
# car.goto(-30, 0)
# car.pendown()
# car.begin_fill()
# car.forward(60)
# car.left(90)
# car.forward(20)
# car.left(90)
# car.forward(60)
# car.left(90)
# car.forward(20)
# car.end_fill()
#
# # Draw the roof and back window of the car
# car.penup()
# car.goto(0, 20)
# car.pendown()
# car.setheading(0)  # Reset angle
# car.forward(30)
# car.left(90)
# car.forward(20)
# car.left(90)
# car.forward(30)
#
# # Draw the wheels of the car
# car.penup()
# car.goto(10, -10)
# car.pendown()
# car.color("black")
# car.begin_fill()
# car.circle(10)
# car.end_fill()
#
# car.penup()
# car.goto(-20, -10)
# car.pendown()
# car.begin_fill()
# car.circle(10)
# car.end_fill()
#
# # Hide the turtle and display the result
# car.hideturtle()
#
# # Keep the window open until it is closed by the user
# t.done()
