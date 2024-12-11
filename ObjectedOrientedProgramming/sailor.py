class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Sailor(Human):
    def __init__(self, name, position):
        Human.__init__(self, name)
        self.position = position

    def get_position(self):
        return self.position


s1 = Sailor('<NAME>', 0)
s2 = Sailor('<NAME>', 1)