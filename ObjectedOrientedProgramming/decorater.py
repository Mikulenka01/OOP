def my_decorator(func):
    def wrapper():
        print("Dekorátor: Funkcia sa začína vykonávať.")
        func()
        print("Dekorátor: Funkcia skončila.")
    return wrapper


@my_decorator
def say_hello():
    print("Ahoj, svet!")


def say_hello2():
    print("Ahoj, svet2!")


# Volanie dekorovanej funkcie
say_hello()
# func

print()
my_decorator(say_hello2)()

print()
say_hello2 = my_decorator(say_hello2)

say_hello2()