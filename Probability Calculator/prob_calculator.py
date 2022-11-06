import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        temp = []
        for key, value in self.__dict__.items():
            color = key
            number = value
            for i in range(number):
                temp.append(color)
        self.contents = temp

    def draw(self, number_to_draw):
        drawed_balls = []
        if number_to_draw > len(self.contents):
            all_balls = copy.deepcopy(self.contents)
            self.contents = []
            return all_balls
        for i in range(number_to_draw):
            drawed_ball = self.contents.pop(i)
            drawed_balls.append(drawed_ball)

        return drawed_balls

    def get_contents(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


x = Hat(red=2, blue=1)

print(x.get_contents())

print(x.draw(2))

print(x.get_contents())