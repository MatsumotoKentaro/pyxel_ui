import pyxel

from mini_ui import Label

pyxel.init(160, 160, "Hello Pyxel")

label = Label("Hello Pyxel", 10, 10, 7)
label.draw()

pyxel.show()
