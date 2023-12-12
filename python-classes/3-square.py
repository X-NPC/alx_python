"""
Does task2 of python classes assignment.
"""
class Square:
    """It improves on 2-squares by including getters and setters """
    def __init__(self, size=0):
        self._Square__size= size
        
    
    @property 
    def size (self):
        return self.__size
    
    @size.setter
    def size(self, value):
        
       if type(value) != int:
            print("size must be an integer")
       elif value < 0:
           print("size must be >= 0 ")
       else:
            pass
    
        
    
    def area(self):
        return self._Square__size**2
    
    

    

