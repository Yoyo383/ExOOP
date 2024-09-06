from shape import Shape


class RectangleAddition(Shape):
    """
    Class that holds the rectangle addition result (area and perimeter).
    """

    def __init__(self, area, perimeter):
        """
        Creates a new instance with an area and a perimeter.
        :param area: The result's area.
        :type area: float
        :param perimeter: The result's perimeter.
        :type perimeter: float
        """
        super().__init__('')
        self.area = area
        self.perimeter = perimeter

    def get_area(self):
        """
        Calculates the shape's area.
        :return: The shape's area
        :rtype: float
        """
        return self.area

    def get_perimeter(self):
        """
        Calculates the shape's perimeter.
        :return: The shape's perimeter
        :rtype: float
        """
        return self.perimeter
