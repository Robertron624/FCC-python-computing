import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


x = Hat(yellow=2, blue=3, orange=10)

print(x.yellow, x.blue)
