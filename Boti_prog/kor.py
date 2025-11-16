#!/usr/bin/env python3

class Sphere:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4/3 * 3.141592653589793 * self.r**3

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __str__(self):
        return f"Sphere(r={self.r})"

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return 3.141592653589793 * self.a * self.b

    def __str__(self):
        return f"Ellipse(a={self.a}, b={self.b})"



def main():
    s1 = Sphere(2)
    s2 = Sphere(3)

    print(s1 < s2)   
    print(s1 >= s2)  

    e = Ellipse(4, 2)
    print(e.area())  


##############################################################################

if __name__ == "__main__":
    main()