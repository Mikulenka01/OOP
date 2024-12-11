from datetime import datetime


def asterix(func):
    def wrapper(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)

    return wrapper



@asterix
def current_time(time_zone):
    print(time_zone)
    print(datetime.now().strftime("%H:%M:%S"))


@asterix
def current_time2(time_zone, foo):
    print(time_zone)
    print(foo)
    print(datetime.now().strftime("%H:%M:%S"))



current_time("Prag")
print()
current_time2("Prag", "foo")