from datetime import datetime


def asterix(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("*" * times)
            func(*args, **kwargs)
            print("*" * times)
        return wrapper
    return decorator



@asterix(10)
def current_time(time_zone):
    print(time_zone)
    print(datetime.now().strftime("%H:%M:%S"))

@asterix(30)
def current_time2(time_zone, foo):
    print(time_zone)
    print(foo)
    print(datetime.now().strftime("%H:%M:%S"))



current_time("Prag")
print()
current_time2("Prag", "foo")