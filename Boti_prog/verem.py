#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.adatok = []

    def betesz(self, x):
        self.adatok.append(x)

    def kivesz(self):
        if self.ures():
            return None
        return self.adatok.pop()

    def meret(self):
        return len(self.adatok)

    def ures(self):
        return len(self.adatok) == 0

    def __str__(self):
        return "[" + " ".join(str(x) for x in self.adatok)



def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)

##############################################################################

if __name__ == "__main__":
    main()
