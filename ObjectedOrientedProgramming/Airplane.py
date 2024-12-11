class Airplane:
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers

    def __str__(self):
        return f"Airplane: {self.name} - capacity: {self.passengers}"

    def __eq__(self, o):
        return self.passengers == o.passengers and self.name == o.name

    def __lt__(self, o):
        return self.passengers < o.passengers

    def __gt__(self, o):
        return self.passengers > o.passengers

    def __add__(self, o):
        return self.passengers + o.passengers




if __name__ == '__main__':
    a1 = Airplane("plane 1", 200)
    a2 = Airplane("plane 1", 100)
    a3 = Airplane("plane 1", 10)
    print(a1)

    print(a1 == a2)
    print(a3 < a2 < a1)

    print(a1 + a2)