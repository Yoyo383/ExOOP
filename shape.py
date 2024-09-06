class Shape:
    """
    Class that represents a shape.
    """

    def __init__(self, color):
        """
        Creates a new shape.
        :param color: The shape's color
        :type color: str
        """
        self.color = color

    def set_color(self, color):
        """
        Sets the shape's color.
        :param color: The new color
        :type color: str
        """
        self.color = color

    def get_color(self):
        """
        Returns the shape's color.
        :return: The shape's color
        """
        return self.color

    def get_area(self):
        """
        Calculates the shape's area.
        :return: The shape's area
        :rtype: float
        """
        pass

    def get_perimeter(self):
        """
        Calculates the shape's perimeter.
        :return: The shape's perimeter
        :rtype: float
        """
        pass
