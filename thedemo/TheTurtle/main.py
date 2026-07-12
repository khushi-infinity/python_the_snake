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


def draw_dashed_lines(length):
    for _ in range(length):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

make_a_square()
draw_dashed_lines(10)

screen = Screen()
screen.exitonclick()