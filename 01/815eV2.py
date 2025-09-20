#!/usr/bin/env python3


def palindrom(s1):
    hossz = len(s1) 
    i = 0
    ertek = 0
    while i < hossz // 2:
        if s1[i].lower() != s1[hossz - i - 1].lower():
            ertek = 1
            break
        i += 1

    if ertek == 0:
        print("A szó palindróm")
    else:
        print("A szó nem palindróm")

def main():
    palindrom("Abba")

##############################################################################

if __name__ == "__main__":
    main()