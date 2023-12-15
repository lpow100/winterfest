import spirals

t = spirals.g_turtle()

while True:
    for thing in spirals.funcs:
        thing(t)
        t.clear()
    t = spirals.g_turtle()
