# from turtle import *

# turtle = Turtle()


# star_size = 5
# turtle.color("purple")
# s
# for x in range(5):
#     turtle.pensize(star_size)
#     turtle.fd(100)
#     turtle.rt(144)


# done()
try:

    class Student:
        num_of_student = 0

        def __init__(self, name, age, country="Unknown"):
            self.__name = name
            self.__age = age
            self.__country = country
            Student.num_of_student += 1

        # encapsulation methodes public => private
        def get_value(self):
            return self.__name

        def set_value(self, new_name):
            self.__name = new_name

        def get_age(self):
            return self.__age

        def set_age(self, new_age):
            self.__age = new_age

        def get_country(self):
            return self.__country

        def set_coutry(self, new_countary):
            self.__country = new_countary

        def say_hello_to(self):
            if self.name.isdigit():
                print("")
                print("please enter your name")

            else:
                print(
                    "Hello {}, you are {} years old and your country is {}".format(
                        self.__name, self.__age, self.__country
                    )
                )

    # user_name = input("Enter your Name: ")
    # user_age = float(input("Enter your Age: "))

    user_name = "Omar"
    user_age = 15.8
    student_1 = Student(user_name, user_age)
    student_1.set_value("Kapten phiso")
    print(student_1.get_value())

    print("")
    print(f" the numer of ogin student is : {Student.num_of_student}")

except TypeError and ValueError:
    print("Please Enter the correct answer")
