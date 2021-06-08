	# Define a class named Shape and its subclass Square.
    # The Square class has an init function which takes length as argument. 
    # Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.


class Shape():
    def __init__(self):
        pass

    def a(self):
        return 0

class Square(Shape):
    def __init__(self, length=0):
        self.length = length
        Shape.__init__(self)
        

    def a(self):
        return self.length*self.length

x = Square(10)
print(x.a())
print(Square().a())