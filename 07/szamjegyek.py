#!/usr/bin/env python3

def main():
    snum = str(2**1000)
    osszeg = 0
    for c in snum:
        osszeg += int(c)

    print(osszeg)


##############################################################################

if __name__ == "__main__":
    main()