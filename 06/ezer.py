#!/usr/bin/env python3

def main():
    osszeg = [n for n in range(1000) if n % 3 == 0 or n % 5 == 0 ]
    print(sum(osszeg))

##############################################################################

if __name__ == "__main__":
    main()