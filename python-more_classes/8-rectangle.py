#!/usr/bin/python3
"""Module that defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle with specific width and height

        Args:
            number_of_instances: by defult equal 0 but we can
            incremented each new instance instantiation
            and decremented each instance deletion.

            print_symbol: by defult equal # but is symbol we
            can change it any time to print another symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the current width of Rectangle."""
        return self.__width

    @property
    def height(self):
        """Gets the cuttent height of Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value for the width

            Args:
                value (int): new width of the Rectangle

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for the height

            Args:
                value (int): new height of the Rectangle

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return: The current area for the Rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Return: The current perimeter for the Rectangle."""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """print: object of the Rectangle.

            Args:
                result: For save the operation with width

            Return: For return the arg result to str()
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        if hasattr(self, 'print_symbol'):
            symbol = str(self.print_symbol)
        else:
            symbol = str(Rectangle.print_symbol)

        result = ""
        for _ in range(self.__height):
            result += symbol * self.__width + "\n"
        return result.rstrip()

    def __repr__(self):
        """Return: Should return a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print: message for user to delete rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1.area()
            elif rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2.area()
