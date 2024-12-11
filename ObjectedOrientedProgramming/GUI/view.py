from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self, name: str, position: (float, float)):
        self.name = name
        self.position = position

    @abstractmethod
    def move(self, new_position: (float, float)):
        pass