#!/usr/bin/env python3

#A program a Nevedet ki irja karakter helyesen, szóval első betű nagy a többi kicsi.

def main():
    s= input("Neved: ")
    s = s.capitalize()
    print("Hello {0}!".format(s))

##############################################################################

if __name__ == "__main__":
    main()