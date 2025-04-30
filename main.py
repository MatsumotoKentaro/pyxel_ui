import pyxel

from mini_ui import Button, Label

pyxel.init(160, 160, "Hello Pyxel")

label = Label("Hello Pyxel", 10, 10, 7)
count = 0


def update_text():
    global label, count
    count += 1
    label.text = f"Pressed:{count}"


button = Button("Hello, Button", update_text, 10, 50, 100, 16, 1, 2)


def update():
    button.update()


def draw():
    pyxel.cls(0)
    label.draw()
    button.draw()


pyxel.run(update, draw)
