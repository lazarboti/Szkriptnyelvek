#!/usr/bin/env python3

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle({w}, {h})".format(w=self.width, h=self.height)

def main():
    r1 = Rectangle(0, 5)
    r2 = Rectangle(10, 20)
    print(r1.area())
    print(r2.area())

##############################################################################

if __name__ == "__main__":
    main()