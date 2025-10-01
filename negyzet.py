#!/usr/bin/env python3


def main():
    r1 = 0  
    for n in range(100+1):
        r1 += n
    r1 = r1*r1
    r2 = 0
    for n in range(100+1):
        r2 += (n*n)
    result = r1-r2
    print("Eredmeny: {0}".format(result))
##############################################################################



if __name__ == "__main__":


    main()