from container import Container
from rectangle import Rectangle
from square import Square
from circle import Circle
import math


def test_shapes():
    """
    Tests the shape methods.
    """
    rect1 = Rectangle(10, 4, 'Red')
    square1 = Square(9, 'Black')
    circle1 = Circle(5, 'Yellow')

    assert rect1.get_area() == 40
    assert rect1.get_perimeter() == 28

    assert square1.get_area() == 81
    assert square1.get_perimeter() == 36

    assert math.isclose(circle1.get_area(), 25 * math.pi)
    assert math.isclose(circle1.get_perimeter(), 10 * math.pi)

    addition = rect1 + square1
    assert addition.get_area() == 121
    assert addition.get_perimeter() == 64


def main():
    """
    The main function.
    """
    container = Container()
    container.generate(100)
    print('Total area:', container.sum_areas())
    print('Total perimeter:', container.sum_perimeters())
    print('Colors:', container.count_colors())


if __name__ == '__main__':
    test_shapes()
    main()
