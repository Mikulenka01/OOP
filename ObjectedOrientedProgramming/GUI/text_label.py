from .view import View
from .display import Display


class TextLabel(Display, View):
    def __init__(self, name: str, position: (float, float), text: str):
        View.__init__(self, name, position)
        self.text = text

    def show(self):
        print(f"name: {self.name}, position: {self.position}, text: {self.text}")

    def move(self, new_position: (float, float)):
        self.position = new_position