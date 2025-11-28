#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.adatok = []

    def betesz(self, x):
        self.adatok.append(x)

    def kivesz(self) -> None:
        if self.ures():
            return None
        return self.adatok.pop()

    def meret(self) -> int:
        return len(self.adatok)

    def ures(self) ->bool:
        return len(self.adatok) == 0

    def __str__(self):
        return "[" + " ".join(str(x) for x in self.adatok)



