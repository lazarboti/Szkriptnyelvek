#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 3:
        print("Nem megfelelő bemenet!")
        return 1
    else:
        osszeg =int(sys.argv[1])+ int(sys.argv[2])
        print(f"Az eredmény {osszeg}")
    

##############################################################################

if __name__ == "__main__":
    main()