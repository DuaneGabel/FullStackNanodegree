#!/usr/bin/env python

import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_shapes():
  draw_square()
#  draw_circle()
#  draw_triangle()

def move(turtle_name, length, angle):
  turtle_name.forward(length)
  turtle_name.right(angle)
 
def draw_square():
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.speed(9)
  brad.color("blue")

  for i in range (0, 36):
    for j in range (0, 4):
      move(brad, 100, 90)
      j += 1
    brad.right(10)
    i += 1

#def draw_circle():
#  angie = turtle.Turtle()
#
#  angie.circle(100)

#def draw_triangle():
#  homer = turtle.Turtle()

#  counter = 0
#  while (counter < 3):
#    move(homer, 200, 120)
#    counter += 1

draw_shapes()

window.exitonclick()
