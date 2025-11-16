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

    def ures(self):
        return len(self.adatok) == 0

    def meret(self):
        return len(self.adatok)

class MyQueue:
    def __init__(self):
        self.instack = Verem()
        self.outstack = Verem()

    def append(self, x):
        self.instack.betesz(x)

    def popleft(self):
        if self.outstack.ures():
            while not self.instack.ures():
                self.outstack.betesz(self.instack.kivesz())
        return self.outstack.kivesz()

    def is_empty(self):
        return self.instack.ures() and self.outstack.ures()

    def size(self):
        return self.instack.meret() + self.outstack.meret()


def main():
    q = MyQueue()
    print(q.is_empty())  
    q.append(10)
    q.append(20)
    q.append(30)
    print(q.size())       
    print(q.popleft())    
    print(q.popleft())    
    print(q.size())       
    print(q.popleft())    
    print(q.popleft()) 

##############################################################################

if __name__ == "__main__":
    main()