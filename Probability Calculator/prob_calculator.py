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

    def draw(self, number_to_draw) -> list:
        drawed_balls = []
        if number_to_draw > len(self.contents):
            return self.contents
        for i in range(number_to_draw):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            drawed_balls.append(ball)
        return drawed_balls

    def get_contents(self):
        return self.contents


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    count = 0
    for _ in range(num_experiments):
        copyhat = copy.deepcopy(hat)
        temp_list = copyhat.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if temp_list.count(key) < value:
                success = False
                break
        if success:
            count += 1
    return count / num_experiments


x = Hat(red=2, blue=1)

print(x.get_contents())

print(x.draw(2))

print(x.get_contents())
