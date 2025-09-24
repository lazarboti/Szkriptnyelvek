#!/usr/bin/env python3

def mult(lista):
    r = 1
    for e in lista:
        r *= e
    return r


def main():

    lista = [2,4,7,8,2,5]
    lista2 = []
    r = mult(lista)
    r2 = mult(lista2)
    print("Az első lista elemeinek szorzata: {0}".format(r))
    print("A második lista elemeinek szorzata: {0}".format(r2))
##############################################################################



if __name__ == "__main__":


    main()