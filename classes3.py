class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):   # initializator method, may remove =0th
        print("__init__ call")
        self.x = x
        self.y = y

    def __del__(self):      # class instance removal  
        print("Instance remove: " + str(self))

    def set_coords(self, x, y):     # function inside of class calls method (+self, to be able to call for method inside of class)     
        self.x = x
        self.y = y

    def get_cords(self):
        return self.x, self.y
    
pt = Point(1, 3)      # class instance
print(pt.__dict__)
