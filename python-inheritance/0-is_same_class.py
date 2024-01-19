"""this should be a function that returns true if a given
objects is an instance in the inherited class, and returns false if not.
"""

#def is_name_class(object, a_class):
    
#Warning: Mesoud's code

def is_same_class(obj, specified_class):
    """
    this function will check if object is exactly instance of 
    a specified class
    
    """
    return type(obj) == specified_class
