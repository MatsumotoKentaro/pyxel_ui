import pyxel

from localstorage import load, save
from mini_ui import Button, Column, Label


class App:
    def __init__(self):
        pyxel.init(160, 160, "mini ui sample")
        pyxel.mouse(True)

        count_load = load("count")
        self.count = int(count_load) if count_load is not None else 0
        self.label = Label(f"click count:{self.count}", color=7)
        self.column = Column(
            0,
            0,
            spacing=12,
            children=[
                Button(
                    "Click",
                    self.update_text,
                    center_x=True,
                    color_text=3,
                    color_rect=2,
                    fill=True,
                ),
                self.label,
            ],
            w=pyxel.width,
            h=pyxel.height,
            align="center",
        )

        pyxel.run(self.update, self.draw)

    def update_text(self):
        self.count += 1
        save("count", f"{self.count}")
        self.label.text = f"click count:{self.count}"

    def update(self):
        self.column.update()

    def draw(self):
        pyxel.cls(0)
        self.column.draw()


App()
