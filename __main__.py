from time import sleep
import spirals
import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)

while True:
    for spiral in spirals.funcs:
        spiral(t, screen)
        sleep(5)
        t.setposition(0, 0)
        t.setheading(0)
        t.clear()
        screen.bgcolor("white")
