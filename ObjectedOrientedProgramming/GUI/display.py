from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def show(self):
        pass