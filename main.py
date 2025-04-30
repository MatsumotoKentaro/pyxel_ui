import pyxel

from mini_ui import Button, Column, Label

pyxel.init(160, 160, "Hello Pyxel")
pyxel.mouse(True)

count = 0
label_text = f"click count:{count}"
label = Label(label_text, color=7)


def update_text():
    global count, label
    count += 1
    label.text = f"click count:{count}"


menu_ui = Column(
    0,
    0,
    spacing=12,
    children=[
        Button("Click", update_text, center_x=True),
        label,
    ],
    w=pyxel.width,
    h=pyxel.height,
    align="center",
)


def update():
    menu_ui.update()


def draw():
    pyxel.cls(0)
    menu_ui.draw()


pyxel.run(update, draw)
