import turtle

from itertools import cycle


def hex_int(num: int) -> str:
    str_hex = hex(num)[2:]
    if len(str_hex) == 1:
        return f"0{str_hex}"
    return str_hex


class hex_color:
    """Looping color that returns hex value for str"""

    def __init__(self, colors: list[int] = [0, 0, 0]) -> None:
        if len(colors) > 3:
            print("Error: too many colors")
            exit(1)
        self.r = colors[0]
        self.b = colors[1]
        self.g = colors[2]

    def add_red(self, amount):
        if self.r + amount > 255:
            self.r = 0
        self.r += amount

    def add_green(self, amount):
        if self.g + amount > 255:
            self.g = 0
        self.g += amount

    def add_blue(self, amount):
        if self.b + amount > 255:
            self.b = 0
        self.b += amount

    def __str__(self) -> str:
        return f"#{hex_int(self.r)}{hex_int(self.g)}{hex_int(self.b)}"


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
    color = hex_color()
    turt.color(str(color))

    w = 1

    sel = 0

    for x in range(100):
        for y in range(3):
            turt.left(360 / 3 + 1)
            turt.forward(w)
            w += 3
            sel += 1
            if sel % 30 <= 10:
                color.add_red(3)
            elif sel % 30 <= 20:
                color.add_green(3)
            elif sel % 30 <= 30:
                color.add_blue(3)
            turt.color(str(color))


def zeb(turt, screen) -> None:
    screen.bgcolor("#FF072F")

    # Begin!
    turt.pensize(3)
    turt.speed(0)
    turt.color("#65FF65")
    turt.penup()
    turt.setposition(-100,0)
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


def nick(turt, screen) -> None:
    # Begin!
    turt.pensize(3)

    turt.penup()
    turt.setposition(-50,100)
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


def samuel(turt, screen) -> None:
    # Begin!
    turt.pensize(2)
    turt.penup()
    turt.setposition(0,-200)
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


def cynthia_velazquez(turt, screen) -> None:
    # Begin!
    turt.pensize(4)
    turt.penup()
    turt.setposition(0,200)
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


def xoe(turt, screen) -> None:
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


def tim(turt, screen):
    # Begin!
    turt.pensize(2)
    turt.speed(0)
    turt.penup()
    turt.setposition(0,200)
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


def sai(turt, screen):
    # Begin!
    turt.pensize(10)
    sides = cycle([1, 2, 3, 4, 5])
    colors = cycle(["#335C67", "#FFF3B0", "#E09F3E", "#9E2A2B", "#540B0E"])

    turt.penup()
    turt.setposition(-100, -300)
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


def ethan_meyer(turt, screen):
    screen.bgcolor("black")

    # Begin!
    turt.speed(0)
    turt.shape("turtle")
    turt.penup()
    turt.setpos(50, 200)
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


def yas(turt, screen):
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


def grace(turt, screen):
    # Begin!
    turt.pensize(5)
    turt.speed(0)
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


def joel(turt, screen):
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


def jake(turt, screen):
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


# all the funcs to run if you add one make sure to put it here
funcs = [
    # sipral1,
    # logan,
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
]
