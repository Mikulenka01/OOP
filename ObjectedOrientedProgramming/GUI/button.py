from .view import View
from .display import Display
from typing import Callable


class Button(Display, View):
    def __init__(self, name: str, position: (float, float), label: str, action: Callable[[], None]):
        View.__init__(self, name, position)
        self.label = label
        self.action = action

    def show(self):
        print(f"name: {self.name}, position: {self.position}, label: {self.label}")

    def on_click(self):
        self.action()

    def move(self, new_position: (float, float)):
        self.position = new_position