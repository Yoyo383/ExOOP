from shape import Shape
from rectangle_add import RectangleAddition


class Rectangle(Shape):
    """
    Rectangle shape.
    """

    def __init__(self, a, b, color):
        """
        Creates a new rectangle.
        :param a: The rectangle's width
        :type a: float
        :param b: The rectangle's height
        :type b: float
        :param color: The rectangle's color
        :type color: str
        """
        super().__init__(color)
        self.a = a
        self.b = b

    def add(self, other):
        """
        Adds the current rectangle with another one.
        :param other: The other rectangle.
        :type other: Rectangle
        :return: A RectangleAddition object that has the area and the perimeter of the result.
        :rtype: RectangleAddition
        """
        return RectangleAddition(self.get_area() + other.get_area(), self.get_perimeter() + other.get_perimeter())

    def __add__(self, other):
        """
        Adds the current rectangle with another one.
        :param other: The other rectangle.
        :type other: Rectangle
        :return: A RectangleAddition object that has the area and the perimeter of the result.
        :rtype: RectangleAddition
        """
        return self.add(other)

    def get_area(self):
        """
        Calculates the shape's area.
        :return: The shape's area
        :rtype: float
        """
        return self.a * self.b

    def get_perimeter(self):
        """
        Calculates the shape's perimeter.
        :return: The shape's perimeter
        :rtype: float
        """
        return 2 * (self.a + self.b)
