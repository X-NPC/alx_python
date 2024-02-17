"""this is doced"""

from models.base import Base

class Rectangle(Base):
    """this class is doc-ed"""
    def __init__(self, width, height, x=0, y=0, id=None):
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

    # Area method
    def area(self):
        return self.width * self.height

    # Display method
    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    # Update method
    def update(self, *args, **kwargs):
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

    # Override __str__ method
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
