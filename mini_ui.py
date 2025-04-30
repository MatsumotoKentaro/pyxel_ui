import pyxel


class Widget:
    def update(self):
        pass

    def draw(self):
        pass


# テキスト表示
class Label(Widget):
    def __init__(self, text, x=0, y=0, color=0):
        self.text = text
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pyxel.text(self.x, self.y, self.text, self.color)
