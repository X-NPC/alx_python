"""hey  I'm back after...I don't know how many days it took to me to come back

 so Im about to work on task-0 of alx python_alomst_cirle proeject.
"""

class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects