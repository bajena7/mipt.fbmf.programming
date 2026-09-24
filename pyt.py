#!/usr/bin/python3
import turtle
def circle(direction="left"):
    N=300
    for i in range(N):
        turtle.forward(1)
        if direction == "left":
            turtle.left(360/N)
        elif direction == "right":
            turtle.right(360/N)
        else:
            print("ERROR")
            return
        turtle.update()
def eight():
    circle("left")
    circle("right")
turtle.tracer(False)
turtle.shape("turtle")
for _ in range(6):
    eight()
    turtle.left(60)
turtle.update()
turtle.done()


