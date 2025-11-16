#!/usr/bin/env python3

class Sor:
    def __init__(self):
        self.adatok = []

    def betesz(self, x):
        self.adatok.append(x)

    def kivesz(self):
        if self.ures():
            return None
        return self.adatok.pop(0)

    def meret(self):
        return len(self.adatok)

    def ures(self):
        return len(self.adatok) == 0

    def __str__(self):
        return "[" + " ".join(str(x) for x in self.adatok)

def main():
    s = Sor()        
    print(s)        
    print(s.ures())  
    s.betesz(10)
    s.betesz(20)
    s.betesz(30)
    print(s)         
    print(s.meret()) 
    x  = s.kivesz()
    print(x)         
    print(s)        
    s.kivesz()
    s.kivesz()
    print(s.kivesz()) 


##############################################################################

if __name__ == "__main__":
    main()