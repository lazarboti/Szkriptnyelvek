#!/usr/bin/env python3

from math import sqrt
import json

def main():
    
    n = 10_000_000
    prim = []
    with open("primes.json", "w") as f:
        lst = [True]*n                      # létrehozunk egy listát, ebben a példában 1000 elemmel
        for i in range(2,int(sqrt(n))+1):     # A lista bejárása a 2 indexértéktől kezdve a korlát gyökéig
            if (lst[i]):                      # Ha a lista i-edik eleme hamis, akkor a többszörösei egy előző ciklusban már hamis értéket kaptak, így kihagyható a következő ciklus.
                for j in range(i*i, n, i):      # a listának azon elemeihez, melyek indexe az i-nek többszörösei, hamis értéket rendelünk
                    lst[j] = False
        for i in range(2,n):                # Kiíratjuk azoknak az elemeknek az indexét, melyek értéke igaz maradt
            if lst[i]:
                prim.append(i)
        result = {
            'primes' : prim
        }
        json.dump(result, f)

##############################################################################

if __name__ == "__main__":
    main()