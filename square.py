from rectangle import Rectangle


class Square(Rectangle):
    """
    Square shape.
    """

    def __init__(self, a, color):
        """
        Creates a new square.
        :param a: The square's side length
        :type a: float
        :param color: The square's color
        :type color: str
        """
        super().__init__(a, a, color)
