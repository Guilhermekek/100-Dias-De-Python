x = 0
def add(*args):
    x = 0
    for i in args:
        x += i
    print(x)

add(1,2,3,4,5)


def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("")

my_car = Car(make="nissan")
print(my_car.model)


def test(*args):
    print(args)


test(1, 2, 3, 5)