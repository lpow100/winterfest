import turtle

from itertools import cycle

def hex_int(num:int) -> str:
    str_hex = hex(num)[2:]
    if len(str_hex) == 1:
        return f'0{str_hex}'
    return str_hex

class hex_color:
    """Looping color that returns hex value for str"""
    def __init__(self,colors:list[int]=[0,0,0]) -> None:
        if len(colors) > 3:
            print("Error: too many colors")
            exit(1)
        self.r = colors[0]
        self.b = colors[1]
        self.g = colors[2]
    def add_red(self,amount):
        if self.r + amount > 255:
            self.r = 0
        self.r += amount
    def add_green(self,amount):
        if self.g + amount > 255:
            self.g = 0
        self.g += amount
    def add_blue(self,amount):
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


def g_turtle()->turtle.Turtle:
    return turtle.Turtle()

def sipral1(turt:turtle.Turtle)->None:
    # Fullscreen the canvas
    screen = turtle.Screen()
    screen.setup(1.0, 1.0)

    # Begin!
    t = turt
    x_start, y_start = t.position()

    doodle = spirolateral(7, 90, [4, 6])

    while True:
        this_spin = doodle.next()
        t.forward(this_spin.move() * 7)
        t.left(this_spin.rotate())
        x, y = t.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break
    

def spiral2(turt:turtle.Turtle)->None:
    # Fullscreen the canvas
    screen = turtle.Screen()
    screen.setup(1.0, 1.0)

    # Begin!
    t = turt
    t.speed(0)
    color = hex_color()
    t.color(str(color))

    w = 1

    sel = 0

    for x in range(100):
        for y in range(3):
            t.left(360 / 3 + 1)
            t.forward(w)
            w += 3
            sel += 1
            if sel%30 <= 10:
                color.add_red(3)
            elif sel%30 <= 20:
                color.add_green(3)     
            elif sel%30 <= 30:
                color.add_blue(3)                                                                                                                                                                                                                                                                                                                                       
            t.color(str(color))


#all the funcs to run if you add one make sure to put it here
funcs = [sipral1,spiral2]
