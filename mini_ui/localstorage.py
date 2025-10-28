import json
import os

try:
    import js  # Pyodide環境
    from pyodide.ffi import jsnull
except ImportError:

    class FileBackedLocalStorage:
        def __init__(self, filename="local_storage.json"):
            self.filename = filename
            self._load()

        def _load(self):
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as f:
                    try:
                        self.storage = json.load(f)
                    except json.JSONDecodeError:
                        self.storage = {}
            else:
                self.storage = {}

        def _save(self):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.storage, f, ensure_ascii=False, indent=2)

        def setItem(self, key, value):
            self.storage[key] = value
            self._save()

        def getItem(self, key):
            return self.storage.get(key)

        def removeItem(self, key):
            if key in self.storage:
                del self.storage[key]
                self._save()

        def clear(self):
            self.storage = {}
            self._save()

    js = type("js", (), {"localStorage": FileBackedLocalStorage()})()


def save(key, value):
    js.localStorage.setItem(key, value)


def load(key):
    # LocalStorageから値を取得
    value = js.localStorage.getItem(key)
    # JsNull（存在しないキー）の場合、Noneを返す
    if value is jsnull:
        return None  # Python側で扱いやすい None に変換
    # 存在する場合は、その値を返す
    return value


def remove(key):
    js.localStorage.removeItem(key)


def clear():
    js.localStorage.clear()
