#!/usr/bin/env python3


def palindrom(s1):

    hossz = len(s1) 
    i = 0
    ertek = True
    while i < hossz // 2:
        if s1[i].lower() != s1[hossz - i - 1].lower():
            ertek = False
            break
        i += 1
    return ertek

def main():

    if palindrom("Abba"):
        print("A szó palindróm")
    else:
        print("A szó nem palindróm")

##############################################################################

if __name__ == "__main__":

    main()