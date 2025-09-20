#!/usr/bin/env python3

def fordit(szam):
    fszam= str(szam)[::-1]
    return int(fszam)

def main():
    szam = 34523
    print(f"Eredeti szam: {szam}")
    fszam =fordit(szam)
    print(f"Forditott szam: {fszam}")
    

##############################################################################

if __name__ == "__main__":
    main()