"""hey  I'm back after...I don't know how many days it took to me to come back

 so Im about to work on task-0 of alx python_alomst_cirle proeject.
"""

class base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            id = "argument value"
        else:
            __nb_objects += 1
            id = "new value"