"""
Does task2 of python classes assignment.
"""
class Square:
    """It improves on 1-squares returning the value of the area"""
    def __init__(self, size=0):
        self._Square__size= size
        
        if type(size) != int:
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0 ")
        else:
            pass
        
    def area(self):
        return self._Square__size**2
    

