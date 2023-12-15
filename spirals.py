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


def sipral1():
    # Fullscreen the canvas
    screen = turtle.Screen()
    screen.setup(1.0, 1.0)

    # Begin!
    t = turtle.Turtle()
    x_start, y_start = t.position()

    doodle = spirolateral(7, 90, [4, 6])

    while True:
        this_spin = doodle.next()
        t.forward(this_spin.move() * 7)
        t.left(this_spin.rotate())
        x, y = t.position()
        if x_start == round(x, 0) and y_start == round(y, 0):
            break
    
    screen.clear()
    turtle.hideturtle()


#all the funcs to run if you add one make sure to put it here
funcs = [sipral1]
