#!/usr/bin/env python3

from enum import Enum,auto

class Allapot(Enum):
    UJ = auto()
    HASZNALT = auto()
    SERULT = auto()

class Termek:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def brutto_ar(self):
        return self.price *1.27
    
    def __str__(self):
        return("Név: {0}: {1} Ft".format(self.name , self.brutto_ar()))

class Elektronika(Termek):
    def __init__(self, name, price, allapot):
        super().__init__(name, price)
        self.allapot = allapot

    def brutto_ar(self):
        if self.allapot in [Allapot.HASZNALT, Allapot.SERULT]:
            return super().brutto_ar()*0.80 
        else:
            return super().brutto_ar()       

    def __str__(self):
        return super().__str__() + f" {self.allapot.name}"
    

def main():
    tv = Elektronika("Samsung TV", 100000, Allapot.SERULT)
    print(tv)

##############################################################################

if __name__ == "__main__":
    main()