"""
Does task-4 of python classes assignment.
"""
class Square:
    """It improves on 3-square.py by by adding a public instance that stdouts the square """
    def __init__(self, size=0):
        self._Square__size= size
        
    
    @property 
    
    def size (self):
        """Getter"""
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
        """it just returns the area"""
        return self._Square__size**2
    
    
    def my_print(self):
        """this is the improvment: it "stdouts"(whatever it means) the square """
        if self._Square__size == 0:
            print("")
        else:
            
            
            for i in (0, self._Square__size ** 2):
               
                stdouts = ""
                n = 1
                x = 1
                if x == n*self._Square__size:
                    #line break
                    x += 1
                    n += 1
                    new_stdouts = stdouts + "# \n"
                    return new_stdouts
                else:
                    new_stdouts = stdouts + "#"
                    return new_stdouts
            print (new_stdouts)
                
                
            


    

