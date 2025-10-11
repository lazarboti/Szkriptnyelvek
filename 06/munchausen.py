#!/usr/bin/env python3

def main():
    for i in range(1000000):
        snum = str(i)
        result = 0
        for c in snum:
            if int(c) == 0:
                result += 0
            else:
                result += (int(c)**int(c))
        if i == result:
            print(i)


##############################################################################

if __name__ == "__main__":
    main()