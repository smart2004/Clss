class Point:            # class
    """Surface axis points class."""
    # pass          
    color = 'red'       # atribute
    circle = 2          # artribute

print(Point.color)  # class attribute call

Point.color = 'black'   # assign new value for attribute
Point.circle            # class attribute call
Point.__dict__          # all class attribute

print(Point.color)      
print(Point.circle)
print(Point.__dict__)

Point.circle = 'A'      # assign new value for attribute
print(Point.circle)

a = Point()             # class instance
b = Point()             # class instance

print(a)                
print(b)


type(a)                 # class type

print(type(a))          


print(type(a) == Point)

print(isinstance(a, Point))


Point.circle = 1        # assign new value for attribute
print(Point.circle)     

print(a.__dict__ and b.__dict__)    # all instance attribute

print(a.color)

a.color = 'green'       # assign new value for instance              
print(a.__dict__)       # print all instance a attribute
print(b.__dict__)       # print all instance b attribute

Point.type_pt = 'disc'
print(Point.type_pt)

setattr(Point, 'prop', 1)       # assing new attribute with new value
print(Point.__dict__)

setattr(Point, 'type_pt', 'square') # assign/update attribute 'type_pt' with new value
print(Point.__dict__)


res = Point.circle  # assing class attribute to variable/instance res
print(res)
print(Point.circle)


# print(Point.a)

# print(getattr(Point, 'a'))

print(getattr(Point, 'a', False))       # return False in case of attribute 'a' unavailable

print(getattr(Point, 'color', False))   # return 'color' attribute as it's available

print(getattr(Point, 'color'))          # RETURN 'color attribute as it's available


print(hasattr(Point, 'prop'))           # check for attribute availability           
print(Point.prop)
del Point.prop                          # delete prop attribute
                                        # unable to delete unavailable attribute


print(hasattr(Point, 'prop'))           # check for attribute availability


print(a.__dict__)                       # check all attributes for a instance                       

del a.color                             # del attribute from instance/object

print(a.__dict__)                       # check all atribute for a instance

a.x = 1                                 # set value for object property
a.y = 2                                 # set value for object property
b.x = 10                                # set value for object property    
b.y = 20                                # set value for object property

print(a.__dict__)                       # check all attributes for a instance
print(b.__dict__)                       # check all attributes for b instance         

print(Point.__doc__)  # Docstring class call
