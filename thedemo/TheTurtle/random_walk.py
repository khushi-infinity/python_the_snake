import turtle as t
import random

# creating turtle object and colormode to all the colors
tim = t.Turtle()
t.colormode(255)


# function for generating random rgb values
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour


# set the shape, and width and speed of the turtle
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")



# colors = ["khaki","steel blue","olive","medium sea green","peru","dark orchid","orange","cadet blue","teal","deep sky blue","gray"]
# list of directions
direction = [0,90,180,270]


#loop for making random path and random colours
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
