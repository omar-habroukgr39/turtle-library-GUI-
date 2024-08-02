# from turtle import *
# root = Turtle()
# screen = Screen()
#
# screen.title("omar project")
# # screen.bgcolor("black")



# root.color("mediumpurple")
# root.begin_fill()
# root.penup()
# root.setpos(0,-120)
# root.pendown()
#
# for i in range(4):
#     root.fd(100)
#     root.lt(90)

# root.color("white")
# root.penup()
# root.home()
# root.pendown()
# root.circle(100)
#
# root.end_fill()
# root.penup()
# root.setpos(150,0)
# root.pendown()
# root.circle(100)
#
# root.end_fill()
# root.penup()
# root.setpos(-150,0)
# root.pendown()
# root.circle(100)
#
# root.end_fill()
# root.penup()
# root.setpos(-300,0)
# root.pendown()
# root.circle(100)



# user_input = int(input("Enter a Number: "))
#
# if user_input == 1:
#     root.shape("turtle")
# elif user_input == 2:
#     root.shape("square")
# elif user_input == 3:
#     root.shape("arrow")
# elif user_input == 4:
#     root.shape("triangle")
# elif user_input == 5:
#     root.shape("triangle")
# else:
#     root.shape("circle")



# root.pencolor("red")
# root.fillcolor("orange")
# root.pensize(10)
# root.speed(7)
# root.begin_fill()
# root.circle(75)
# screen.bgcolor("blue")
# root.end_fill()

# root.shape("Turtle")
# root.color("yellow")
# screen.delay(500)
# root.shapesize(20,20,20)
# screen.delay(500)
#
# root.color("red")
#
# root.shape("turtle")
# screen.delay(500)
# root.shapesize(30,30,30)
# screen.delay(500)
#
# root.shape("square")
# root.color("blue")
# screen.delay(500)
# root.shapesize(50,50,50)
# screen.delay(500)
#
# root.color("green")
# root.shapesize(20,20,20)
# screen.delay(500)
# root.shapesize(30,30,30)
#
# root.color("darkorange")
# root.begin_fill()
# root.pencolor("blueviolet")
#
# root.goto(100,100)
# root.goto(100,-100)
# root.goto(-100,100)
# root.goto(-100,-100)
# root.goto(100,100)
#
# root.end_fill()
# root.home()
# root.begin_fill()
# root.pencolor("black")
# root.dot(50,"green")
# root.end_fill()
# root.hideturtle()



# class Student:
# #     def __init__(self, name , age = 0  , countary = " unknowen") :
# #         self.name = name
# #         self.age = age
# #         self.countary = countary
# # student1 = Student("omar")
# # print(student1.countary)

class Animal :
    def __init__(self , name ):
        self.name = name
    def make_sound(self):
      pass

class dog(Animal):
    def make_sound(self):
      print("woof")
class cat(Animal):
    def make_sound(self):
      print("meow")

my_dog = dog("Buddy")
# my_dog.name()
my_dog.make_sound()
my_cat = cat("filler")
print(my_cat.name)
my_cat.make_sound()


# done()