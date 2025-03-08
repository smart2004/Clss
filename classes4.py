class Point:
    def __new__(cls, *args, **kwargs):  # calls prior class object creation, *args/kwargs** are for arguments
        print('call __new__ for ' + str(cls))
        return super().__new__(cls)  # return ref. address for new created object

    def __init__(self, x=0, y=0):  # calls after class object creation
        print('call __init__ for ' + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)        
print(pt)
