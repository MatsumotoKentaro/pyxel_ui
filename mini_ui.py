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


# ボタン（矩形＋テキスト＋クリック）
class Button(Widget):
    def __init__(
        self, text, on_pressed, x=0, y=0, w=50, h=16, color_text=1, color_rect=1
    ):
        self.text = text
        self.on_pressed = on_pressed
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_text = color_text
        self.color_rect = color_rect

    def update(self):
        if (
            pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
            and self.x <= pyxel.mouse_x <= self.x + self.w
            and self.y <= pyxel.mouse_y <= self.y + self.h
        ):
            self.on_pressed()

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color_rect)
        pyxel.text(self.x + 4, self.y + 4, self.text, 0)


# 縦に並べるレイアウト
class Column(Widget):
    def __init__(self, x, y, spacing=8, children=[], center=True):
        self.x = x
        self.y = y
        self.spacing = spacing
        self.children = children
        self.center = center
        self._layout()

    def _layout(self):
        total_height = len(self.children) * self.spacing
        offset_y = self.y - total_height // 2 if self.center else self.y
        for i, child in enumerate(self.children):
            child.x = self.x - pyxel.FONT_WIDTH * len(getattr(child, "text", "")) // 2
            child.y = offset_y + i * self.spacing

    def update(self):
        for child in self.children:
            child.update()

    def draw(self):
        for child in self.children:
            child.draw()
