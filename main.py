import pyxel

from mini_ui import Button, Column, Label

pyxel.init(160, 160, "Hello Pyxel")

label = Label("Hello Pyxel", 10, 10, 7)
count = 0


def update_text():
    global label, count
    count += 1
    label.text = f"Pressed:{count}"


button = Button("Hello, Button", update_text, 10, 50, 100, 16, 1, 2)

menu_ui = Column(
    64,
    64,
    spacing=12,
    children=[
        label,
        button,
    ],
)


def update():
    menu_ui.update()


def draw():
    pyxel.cls(0)
    menu_ui.draw()


pyxel.run(update, draw)
