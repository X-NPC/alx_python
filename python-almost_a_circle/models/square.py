from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the square. Defaults to 0.
            id (int, optional): The unique identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)  # Call the superclass constructor with size as width and height

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
