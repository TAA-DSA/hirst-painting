import random

import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('hirst_painting_img.jpg', 6)


angela = Turtle()
screen = Screen()
screen.colormode(255)
angela.penup()
angela.hideturtle()

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_tuple_list = (r, g, b)
    color_list.append(new_tuple_list)
print(color_list)


angela.setheading(225)
angela.forward(300)
angela.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots):
  angela.penup()
  angela.dot(20, random.choice(color_list))
  angela.forward(50)


  if dot_counts % 10 == 0:

    angela.setheading(90)
    angela.forward(50)
    angela.setheading(180)
    angela.forward(500)
    angela.setheading(0)




# angela.dot(20)

screen.exitonclick()