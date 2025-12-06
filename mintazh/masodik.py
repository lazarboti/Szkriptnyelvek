#!/usr/bin/env python3

from jelszomodule import general_jelszo

def main():
    try:
        inp = input("Adj meg egy számot: ")
        print(general_jelszo(int(inp)))

    except ValueError:
        print("Nem megfelelő bemenet")

##############################################################################

if __name__ == "__main__":
    main()