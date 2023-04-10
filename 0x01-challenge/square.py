#!/usr/bin/python3

class Square:
    
    width = 0
    height = 0

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width ** 2

    def PerimeterOfMySquare(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return "Square with width {} and height {}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.PerimeterOfMySquare())
