import random
from turtle import Turtle, Screen
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
screen = Screen()
#simple draw square
#for i in range(4):
#    timmy.forward(100)
#    timmy.right(90)

#Draw a dashed line
#dash_size = 20

#for _ in range(50//dash_size + 1):
#    timmy.forward(dash_size)
#    timmy.penup()
#    timmy.forward(dash_size)
#    timmy.pendown()

colors = [
    "gainsboro",
    "light gray",
    "silver",
    "dark gray",
    "gray",
    "dim gray",
    "black"
]
# Draw multiple geometry forms
#for sides in range(3, 10):
#    timmy.color(colors[sides-3])
#    for _ in range(sides):
#        timmy.forward(100)
#        timmy.right(360/sides)

rotations = [
    0,
    90,
    180,
    270
]
speed = [
    "slowest",
    "slow",
    "normal",
    "fast",
    "fastest"
]
#Draw a random walk
#for _ in range(1000):
#    rotation = random.choice(rotations)
#    color = random.choice(colors)
#    timmy.color(color)
#    timmy.speed(random.choice(speed))
#    timmy.pensize(3)
#    timmy.forward(30)
#    timmy.setheading(rotation)

#Draw multiple circles

#timmy.speed("fast")
#for i in range(10, 360, 10):
#    timmy.color(random.choice(colors))
#    timmy.circle(100)
#    timmy.right(10)
#colors = colorgram.extract('download.webp', 30)
#colors_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#print(colors_rgb)
#Draw a Hirst Painting
colors = [  (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
(217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126
, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
timmy.hideturtle()
timmy.penup()
timmy.setposition(-220, -250)
timmy.pendown()
screen.colormode(255)
timmy.speed("fastest")
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    timmy.setposition(-220, timmy.pos()[1] + 50)
    timmy.pendown()



screen.exitonclick()