"""
Does task2 of python classes assignment.
"""
class Square:
    """It improves on 0-squares by raising type error and value error for wrong inputs """
    
    def __init__(self, size=0):
        self._Square__size= size
        
        if type(size) != int:
            print("size must be an integer")
        else:
            pass
        if size >= 0:
            pass
        else:
            print("size must be >= 0 ")
       
