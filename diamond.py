#!/usr/bin/env python3

import sys

def main():
    n = int(input("Adjon meg egy páratlan számot: ") )
    if n % 2 == 0:
        print("Hiba nem megfeleő bemenet!", file=sys.stderr)
        return 1
    i = 1
    while i <= n:
        for k in range((n - i) // 2):
            print(" ",end='')
        for k in range(i):
            print("*",end='')
        for k in range((n - i) // 2):
            print(" ",end='')
        print("")
        i += 2
    
    i -= 2+2
    while i >= 1:
        for k in range((n - i) // 2):
            print(" ",end='')
        for k in range(i):
            print("*",end='')
        for k in range((n - i) // 2):
            print(" ",end='')
        print("")
        i -= 2
    
    return 0


    
##############################################################################



if __name__ == "__main__":


    main()