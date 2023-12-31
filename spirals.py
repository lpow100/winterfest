import random
import turtle
from itertools import cycle



class spin:
    def __init__(self, len: int, rot: int) -> None:
        self.__mov__ = len
        self.__rot__ = rot

    def move(self):
        return self.__mov__

    def rotate(self):
        return self.__rot__


class spirolateral:
    def __init__(self, size: int, rotation: int, flips: list[int] = []):
        self.rotation = rotation
        self.flips = flips
        self.turns = cycle(range(1, size + 1))

    def next(self):
        pos = next(self.turns)
        if pos in self.flips:
            if self.rotation + 180 > 360:
                return spin(pos, self.rotation - 180)
            else:
                return spin(pos, self.rotation + 180)
        else:
            return spin(pos, self.rotation)


def sipral1(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # Begin!
    x_start, y_start = turt.position()
    turt.speed(0)
    turt.pensize(5)

    doodle = spirolateral(7, 90, [4, 6])

    while True:
        this_spin = doodle.next()
        turt.forward(this_spin.move() * 14)
        turt.left(this_spin.rotate())
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def logan(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # Begin!
    turt.speed(0)
    turt.pensize(1)
    sel = 0
    turtle.colormode(255)
    turt.pencolor(
        random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)
    )

    w = 1

    for x in range(100):
        for y in range(3):
            turt.left(360 / 3 + 1)
            turt.forward(w)
            w += 3
            sel += 1
            if sel % 10 == 0:
                turt.pencolor(
                    random.randint(30, 255),
                    random.randint(30, 255),
                    random.randint(30, 255),
                )


def zeb(turt: turtle.Turtle, screen) -> None:
    screen.bgcolor("#FF072F")
    # Begin!
    turt.pensize(3)
    turt.speed(0)
    turt.color("#fabc02")
    turt.penup()
    turt.setposition(-100, 0)
    turt.pendown()

    sides = cycle([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.forward(40 * side)
        turt.left(155)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def nick(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # Begin!
    turt.pensize(3)

    turt.penup()
    turt.setposition(-50, 100)
    turt.pendown()
    sides = cycle([2, 4, 1, 3, 2, 4, 3, 5, 4, 6])
    colors = cycle(["#FF12A4", "#12FFD6", "#4DB28B", "#E41B42", "#16E946"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(50 * side)
        turt.left(110)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def samuel(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # egin!
    turt.pensize(2)
    turt.penup()
    turt.setposition(0, -200)
    turt.pendown()
    sides = cycle([2, 6, 4, 4, 10])
    colors = cycle(["#99D5C9", "#6C969D", "#645E9D", "#726DA8", "#8661C1"])
    x_start, y_start = turt.position()
    while True:
        turt.shape("turtle")
        side = next(sides)
        turt.color(next(colors))
        turt.forward(45 * side)
        turt.left(55)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def cynthia_velazquez(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # Begin!
    turt.pensize(4)
    turt.penup()
    turt.setposition(0, 200)
    turt.pendown()
    sides = cycle([9, 5, 7, 3, 5])
    colors = cycle(["#5DA5F7", "#379F56", "#5471E3", "#26C5B1", "#8DC59A"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(30 * side)
        turt.left(137)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def xoe(turt: turtle.Turtle, screen: turtle.Screen) -> None:
    # Begin!
    turt.pensize(8)

    sides = cycle([3, 7, 2, 2, 1])
    colors = cycle(["#DCCCFF", "#E07BE0", "#932F6D", "#420039", "#F6F2FF"])
    turt.penup()
    turt.setposition(-200, -100)
    turt.pendown()
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(45 * side)
        turt.left(45)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def tim(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(2)
    turt.speed(0)
    turt.penup()
    turt.setposition(0, 200)
    turt.pendown()
    sides = cycle([5, 3, 7, 4.4, 6, 1, 9])
    colors = cycle(["#6c676b", "#090e27", "#6c676b", "#090e27"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(45 * side)
        turt.left(290)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def sai(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(10)
    sides = cycle([1, 2, 3, 4, 5])
    colors = cycle(["#335C67", "#FFF3B0", "#E09F3E", "#9E2A2B", "#540B0E"])

    turt.penup()
    turt.setposition(0, -200)
    turt.pendown()
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(60 * side)
        turt.left(45)
        x, y = turt.position()
        if x_start == round(x, 3) and y_start == round(y, 0) and turt.heading() == 0:
            break


def ethan_meyer(turt: turtle.Turtle, screen: turtle.Screen):
    screen.bgcolor("black")
    turt.speed(0)
    turt.shape("turtle")
    turt.penup()
    turt.setpos(0, 300)
    turt.pendown()
    sides = cycle([5, 3, 7, 4.4, 6])
    x_start, y_start = turt.position()
    colors = cycle(["#0091AD", "#B37BA4", "#390099"])
    turt.pensize(5)
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(25 * side)
        turt.left(290)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def yas(turt: turtle.Turtle, screen: turtle.Screen):
    # begin
    sides = cycle([0, 2, 3, 2.2, 3, 1])
    colors = cycle(["purple", "blue", "purple", "blue", "purple"])
    x_start, y_start = turt.position()
    turt.pensize(6)
    turt.speed(0)

    while True:
        turt.color(next(colors))
        side = next(sides)
        turt.forward(30 * side)
        turt.left(290)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def grace(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(5)
    turt.speed(0)
    turt.penup()
    turt.setpos(-200, 0)
    turt.pendown()
    sides = cycle([5, 2, 3, 6, 2, 1, 1, 5, 3, 6])
    colors = cycle(["#FFCDB2", "#FFB4A2", "#E5989B", "#B5838D", "#6D6875"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(30 * side)
        turt.left(80)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def joel(turt: turtle.Turtle, screen: turtle.Screen):
    # Fullscreen the canvas
    screen.bgcolor("#222021")
    # Begin!
    turt.color("#222021")
    turt.penup()
    turt.setposition(-100, 0)
    turt.pendown()
    turt.shape("turtle")
    turt.pensize(5)
    turt.speed(0)
    sides = cycle([1, 2, 3, 4, 5])
    colors = cycle(["#FFB2E6", "#6610F2", "#D972FF", "#8447FF", "#8CFFDA", "#FFFFE8"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(90 * side)
        turt.left(901)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def jake(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(5)
    turt.speed(0)
    turt.penup()
    turt.setposition(-100, -200)
    turt.pendown()
    sides = cycle(
        [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    )
    colors = cycle(["#B284BE", "#468284", "#57A0D2", "#9966CB", "#29AB87"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(20 * side)
        turt.left(165)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def ethan_nobel(turt: turtle.Turtle, screen: turtle.Screen):
    screen.bgcolor("#5F4BB6")

    # Begin!
    turt.shape("circle")
    turt.color("#FE621D")
    turt.pensize(7)
    turt.speed(0)
    turt.penup()
    turt.setposition(-100, 200)
    turt.pendown()

    sides = cycle([1, 1, 5, 5, 9, 9, 13, 13, 17, 17])
    x_start, y_start = turt.pos()
    while True:
        side = next(sides)
        turt.forward(5 * side)
        turt.left(110)
        x, y = turt.pos()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def ethan_nobel2(turt: turtle.Turtle, screen: turtle.Screen):
    screen.bgcolor("#c30022")
    screen.tracer(0, 0)
    # Begin!
    turt.shape("turtle")
    turt.speed(0)
    turt.color("#00a53c")
    turt.circle(0)
    turt.pensize(2)

    def draw_spiral(x, y):
        turt.penup()
        turt.setposition(x, y)
        turt.pendown()
        sides = 3
        distance = 3
        for side in range(300):
            turt.forward(distance)
            turt.left(360 / sides + 1)
            distance += 2
            if side % 2 == 0:
                screen.update()

    draw_spiral(200, 0)
    draw_spiral(-200, 0)
    draw_spiral(0, -200)
    draw_spiral(0, 200)
    draw_spiral(250, 250)
    draw_spiral(-250, 250)
    draw_spiral(250, -250)
    draw_spiral(-250, -250)
    screen.tracer(1, 1)


def sanvi(turt: turtle.Turtle, screen: turtle.Screen):
    screen.bgcolor("#BFFFA9")

    # Begin!
    turt.shape("turtle")
    turt.speed(0)
    turt.pensize(10)

    colors = ["#386641", "#6a994e", "#a7c957", "#da2c38", "#f2e8cf"]

    sides = 3.5
    distance = 40

    turt.penup()
    turt.setposition(-30, 0)
    turt.pendown()

    for _ in range(30):
        for color in colors:
            turt.color(color)
            turt.forward(distance)
            turt.left(360 / sides + 0.01)
            distance += 3


def maya(turt: turtle.Turtle, screen: turtle.Screen):
    turt.speed(0)
    turt.pensize(3)
    turt.penup()
    turt.setposition(50, 300)
    turt.pendown()
    sides = cycle([1, 2, 3, 4, 5])
    colors = cycle(["#3D348B", "#FA003F", "#7678ED", "#F7B801", "#F18701", "#F35B04"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(50 * side)
        turt.left(322)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break


def zeb2(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    screen.bgcolor("black")
    turt.pensize(7)
    turt.speed(0)
    turt.shape("circle")
    turt.color("#39E3CB")
    turt.penup()
    turt.setposition(100, 0)
    turt.pendown()

    sides = cycle([7, 9, 3, 5, 2])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.forward(20 * side)
        turt.left(150)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def jack(turt: turtle.Turtle, screen: turtle.Screen):
    turt.speed(0)
    screen.tracer(0, 0)
    turt.pensize(3)
    turt.penup()
    turt.setposition(-300, -225)
    turt.pendown()
    sides = cycle([9, 7, 6, 2, 8, 3, 3, 4, 6, 5, 3, 11, 4])
    colors = cycle(["red", "orange", "yellow", "green", "blue", "purple"])
    x_start, y_start = turt.position()
    counter = 0
    while True:
        turt.color(next(colors))
        side = next(sides)
        turt.forward(45 * side)
        turt.left(69)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break
        if counter % 2 == 0:
            screen.update()
    screen.update()
    screen.tracer(1, 1)


def peyton(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(5)
    turt.speed(0)
    turt.penup()
    turt.setposition(-200, 250)
    turt.pendown()

    sides = cycle([4, 3, 2, 3, 4])
    colors = cycle(["blue", "black", "light blue", "dark blue"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(24 * side)
        turt.right(75)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def lylah(turt: turtle.Turtle, screen: turtle.Screen):
    turt.pensize(7)

    turt.penup()
    turt.setposition(-100, -105)
    turt.pendown()
    sides = cycle([3, 5, 7, 6, 9, 10, 8])
    colors = cycle(["#9d0208", "#006400", "#9d0208", "#006400", "#9d0208", "#006400"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(30 * side)
        turt.left(90)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def owen(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(5)
    turt.speed(0)
    turt.penup()
    turt.setposition(-200, -100)
    turt.pendown()
    sides = cycle([3, 2, 2, 3])
    colors = cycle(["#0B1D51", "#5E2BFF", "#343E3D", "#F5853F", "#E7DE8E"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(40 * side)
        turt.left(100)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def adaline(turt: turtle.Turtle, screen: turtle.Screen):
    # Begin!
    turt.pensize(4)
    turt.shape("turtle")
    turtle.bgcolor("black")
    sides = cycle([1, 2, 3, 4, 5, 6, 7, 8, 9])
    colors = cycle(["#D24343", "#3AA928", "#A9284A", "#054D1D", "#751414", ""])
    turt.penup()
    turt.setposition(-7, -105)
    turt.pendown()
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(19 * side)
        turt.left(114)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def stella(turt: turtle.Turtle, screen: turtle.Screen):
    turt.pensize(8)
    sides = cycle([6, 7, 8, 9, 2])
    colors = cycle(["#00BD48", "#8012D1", "#30B3FD", "#123BD1", "#12D187"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(30 * side)
        turt.left(90)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:
            break


def daisy(turt: turtle.Turtle, screen: turtle.Screen):
    turt.pensize(7)
    turt.shape("turtle")
    turt.speed(0)

    turt.penup()
    turt.setposition(-150, 175)
    turt.pendown()
    sides = cycle([4, 7, 9, 4, 7, 9, 4, 7, 9])
    colors = cycle(["#FFDB00", "#7BDFF2", "#FF6F59"])
    x_start, y_start = turt.position()
    while True:
        side = next(sides)
        turt.color(next(colors))
        turt.forward(15 * side)
        turt.left(126)
        x, y = turt.position()
        if x_start == round(x, 0) and y_start == round(y, 0) and turt.heading() == 0:  # noqa: E501
            break


# def adaline(turt: turtle.Turtle, screen: turtle.Screen):
# all the funcs to run if you add one make sure to put it here
funcs = [
    peyton,
    lylah,
    sipral1,
    adaline,
    daisy,
    stella,
    owen,
    logan,
    zeb,
    nick,
    samuel,
    cynthia_velazquez,
    xoe,
    tim,
    sai,
    ethan_meyer,
    yas,
    grace,
    joel,
    jake,
    ethan_nobel,
    ethan_nobel2,
    sanvi,
    maya,
    jack,
    zeb2,
]
