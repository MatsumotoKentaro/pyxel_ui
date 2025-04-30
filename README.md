# mini_ui

Pyxel向けの軽量UIフレームワーク  
ボタンやラベルなどの基本的なウィジェットをサポートし、縦並びのUIレイアウトを簡単に構築できます。

## 特徴

- Pyxelに簡単なGUI機能を追加
- ウィジェットの描画・イベント処理を一元管理
- `Column` による縦方向レイアウト
- 最小限の構成でPyxelと親和性が高い

## 対応ウィジェット

- `Label`: テキスト表示
- `Button`: クリックイベント対応ボタン
- `Column`: 縦にウィジェットを並べるコンテナ

## インストール

このファイル（`mini_ui.py`）をプロジェクトにコピーしてください。依存ライブラリは `pyxel` のみです。

```bash
pip install pyxel
```

## 使い方

```python
import pyxel

from mini_ui import Button, Column, Label


class App:
    def __init__(self):
        pyxel.init(160, 160, "mini ui sample")
        pyxel.mouse(True)

        self.count = 0
        self.label = Label(f"click count:{self.count}", color=7)
        self.column = Column(
            0,
            0,
            spacing=12,
            children=[
                Button("Click", self.update_text, center_x=True),
                self.label,
            ],
            w=pyxel.width,
            h=pyxel.height,
            align="center",
        )

        pyxel.run(self.update, self.draw)

    def update_text(self):
        self.count += 1
        self.label.text = f"click count:{self.count}"

    def update(self):
        self.column.update()

    def draw(self):
        pyxel.cls(0)
        self.column.draw()


App()

```

## クラス概要

### `Widget`

- 全てのUI部品のベースクラス
- メソッド:
  - `update()`: 入力イベント処理
  - `draw()`: 描画処理

### `Label`

- テキストを表示するウィジェット
- 属性:
  - `text`: 表示する文字列
  - `color`: テキストの色（デフォルトは白）

### `Button`

- ラベル付きのボタン
- 属性:
  - `w`, `h`: ボタンの幅と高さ
  - `text`: ボタンに表示するテキスト
- メソッド:
  - `on_click()`: クリック時に実行されるコールバック関数（初期化時に渡す）

### `Column`

- 縦方向にウィジェットを自動的に並べるコンテナ
- 属性:
  - `x`, `y`: 表示開始位置
  - `spacing`: 各ウィジェットの間隔（ピクセル単位）
- メソッド:
  - `update()`: すべての子ウィジェットの更新処理
  - `draw()`: すべての子ウィジェットの描画処理

## ライセンス

MIT License
