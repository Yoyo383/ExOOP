from shape import Shape
import math


class Circle(Shape):
    """
    Circle shape.
    """

    def __init__(self, radius, color):
        """
        Creates a new circle.
        :param radius: The circle's radius
        :type radius: float
        :param color: The circle's color
        :type color: str
        """
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        """
        Calculates the shape's area.
        :return: The shape's area
        :rtype: float
        """
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        """
        Calculates the shape's perimeter.
        :return: The shape's perimeter
        :rtype: float
        """
        return 2 * math.pi * self.radius
