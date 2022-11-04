class Rectangle:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        pass

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> int:
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self) -> str:

        width = self.width
        height = self.height

        if width > 50 or height > 50:
            return "Too big for picture."

        picture = ""

        row = "*" * width

        for i in range(height):
            picture += f"{row}\n"

        return picture

    def get_amount_inside(self, Rectangle) -> int:
        rectangle_area = Rectangle.get_area()
        this_area = self.get_area()
        
        return int(this_area / rectangle_area)


class Square(Rectangle):

    def __init__(self, side) -> None:
        self.side = side
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.side})"

    def set_side(self, side) -> None:
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, height) -> None:
        self.height = height
        self.width = height
        self.side = height

    def set_width(self, width) -> None:
        self.width = width
        self.height = width
        self.side = width

    

# TEST 1
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())


# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))


# TEST 2

sq = Square(10)

sq.set_side(2)
print(sq)