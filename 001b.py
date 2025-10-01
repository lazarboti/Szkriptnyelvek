#!/usr/bin/env python3


def main():
    osszeg = 0

    for n in range(1,100+1):
         s = str(n)
         lista = list(s)
         for k in lista:
             
             osszeg += int(k)
    
    print(osszeg)


##############################################################################



if __name__ == "__main__":


    main()