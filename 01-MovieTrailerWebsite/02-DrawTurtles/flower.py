#!/usr/bin/env python

import turtle

# set up window
window = turtle.Screen()
window.bgcolor("white")

# define the turtle
brad = turtle.Turtle()
brad.shape("turtle")
brad.speed(9)
brad.color("blue")

# define diamond
leg = 100
wide = 20
narrow = 160

# move function
def move(length, angle):
  brad.forward(length)
  brad.right(angle)

def draw_flower():

  # draw the petals
  for i in range (0, 45):
    for j in range (0, 2):
      move(leg, wide)
      move(leg, narrow)
      j += 1

    brad.right(8)
    i += 1

  # draw the stem
  brad.right(90)
  brad.forward(300)

draw_flower()


window.exitonclick()
