class Rectangle:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        pass

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        return self.picture

    def get_amount_inside(self, figure):
        amount_in_size = 0

        return amount_in_size


class Square(Rectangle):
    pass


x = Square(31)

print(x.get_perimeter())