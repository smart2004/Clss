class Point:
    color = 'red'
    circle = 2

    def set_coords(self):    # methods are also class attributes   
        print('set_cords method call' + str(self))

print(Point.set_coords)

# print(Point.set_coords())


pt = Point()

print(pt.set_coords)
print(pt.set_coords())

print(Point.set_coords(pt))

class Point2:

    def set_coords2(self, x, y):    # methods are also class attributes
        self.x = x
        self.y = y

    def get_cords2(self):   # methods are also class attributes
        return (self.x, self.y)

pt2 = Point2()
pt22 = Point2()
pt2.set_coords2(1, 5)
pt22.set_coords2(3, 6)
print(pt2.__dict__)
print(pt22.__dict__)

f = getattr(pt2, 'get_cords2')
print(f())

ff = getattr(pt22, 'get_cords2')
print(ff())
