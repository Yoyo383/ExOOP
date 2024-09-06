import random
from square import Square
from rectangle import Rectangle
from circle import Circle


class Container:
    """
    Shape container.
    """

    COLORS = ['Red', 'Yellow', 'Blue', 'Green', 'Brown', 'Black', 'White', 'Pink', 'Orange', 'Cyan']
    SHAPE_OPTIONS = ['Square', 'Rectangle', 'Circle']
    MIN_LENGTH = 1
    MAX_LENGTH = 10

    def __init__(self):
        """
        Creates a new shape container.
        """
        self.shapes = []  # Shape[]

    def generate(self, x):
        """
        Generates x random shapes.
        :param x: The number of shapes.
        :type x: int
        """
        for i in range(x):
            shape_name = random.choice(self.SHAPE_OPTIONS)
            color = random.choice(self.COLORS)

            if shape_name == 'Square':
                self.shapes.append(Square(random.uniform(self.MIN_LENGTH, self.MAX_LENGTH), color))
            elif shape_name == 'Rectangle':
                self.shapes.append(Rectangle(random.uniform(self.MIN_LENGTH, self.MAX_LENGTH),
                                             random.uniform(self.MIN_LENGTH, self.MAX_LENGTH),
                                             color))
            elif shape_name == 'Circle':
                self.shapes.append(Circle(random.uniform(self.MIN_LENGTH, self.MAX_LENGTH), color))

    def sum_areas(self):
        """
        Calculates the sum of all the shapes' areas.
        :return: The sum of all areas.
        :rtype: float
        """
        result = 0
        for shape in self.shapes:
            result += shape.get_area()
        return result

    def sum_perimeters(self):
        """
        Calculates the sum of all the shapes' perimeters.
        :return: The sum of all perimeters.
        :rtype: float
        """
        result = 0
        for shape in self.shapes:
            result += shape.get_perimeter()
        return result

    def count_colors(self):
        """
        Counts for each color how many shapes there are with that color.
        :return: A dictionary that maps the color to the number of shapes it has.
        :rtype: dict[str, int]
        """
        result = dict.fromkeys(self.COLORS, 0)
        for shape in self.shapes:
            result[shape.color] += 1
        return result
