# Warning: Mesoud's code

"""
This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """
    This is an empty class that serves as a base for geometry-related classes.
    """
    def area(self):
        """
        This is a method that raises an exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
