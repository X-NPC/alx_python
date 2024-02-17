"""This module defines the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """This class represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the rectangle. Defaults to 0.
            id (int, optional): The unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)  # Call the superclass constructor
        
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None

        # Use setters to validate and set values
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter methods for width, height, x, and y (same as before)

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Variable length arguments to update the rectangle attributes.
            **kwargs: Arbitrary keyword arguments to update the rectangle attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
