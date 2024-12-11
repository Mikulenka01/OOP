class Animal:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello iam {self.name}")


class Dog(Animal):
    def make_sound(self):
        print("hav hav")


class Retriver(Dog):
    def play(self):
        print("aport")


class Bird(Animal):
    def make_sound(self):
        print("pip pip")

"""d1 = Dog("Dunco")
d1.say_hello()

r1 = Retriver("Dunco 2")
r1.say_hello()
r1.make_sound()
r1.play()

b1 = Bird("Bird")
b1.say_hello()


print(Retriver.mro())"""



class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class EBook(File, Book):
    def __init__(self, name, pages, size):
        Book.__init__(self, name, pages)
        File.__init__(self, name, size)

print()
eb = EBook("<NAME>", 100, 100)
print(eb.pages)
print(eb.name)
print(eb.size)
print(EBook.mro())