#!/usr/bin/env python3


import sys
import os

def main():

    name = os.path.basename(sys.argv[0])
    if name == "z-a.py":
        reverse = True
    else:
        reverse = False
    betuk = [chr(c) for c in range(97, 122+1)]
    if reverse:
        betuk = betuk[::-1]
    for b in betuk:
        print(b,end="")
        
##############################################################################

if __name__ == "__main__":
    main()