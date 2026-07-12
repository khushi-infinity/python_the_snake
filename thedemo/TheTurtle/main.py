from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

def forward_turn_left():
    timmy.forward(100)
    timmy.left(90)

def make_a_square():
    for i in range(4):
        forward_turn_left()


make_a_square()

screen = Screen()
screen.exitonclick()