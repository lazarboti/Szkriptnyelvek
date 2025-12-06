#!/usr/bin/env python3

def main():
    lista = []
    with open("versenyzok.txt" ,"r") as f:
        for line in f:
            line = line.rstrip("\n")
            tomb =line.split(";")
            lista.append(tomb)


    lista  =sorted(lista, key= lambda x: int(x[1]) )
    for p in lista:
        print("{0:^20}".format(p[0]))


##############################################################################

if __name__ == "__main__":
    main()