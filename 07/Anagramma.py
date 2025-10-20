#!/usr/bin/env python3

def anagramm2(szo1, szo2):
    tomb = list(szo1.replace(" ","").lower())
    tomb2 = list(szo2.replace(" ","").lower())
    d1 = {}
    d2 = {}
    for c in tomb:
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1
    for c in tomb2:
        if c in d2:
            d2[c]  += 1
        else:
            d2[c] = 1

    if sorted(d1) == sorted(d2):
        return True
    else:
        return False


def anagramm(szo1, szo2):
    tomb = list(szo1.replace(" ","").lower())
    tomb2 = list(szo2.replace(" ","").lower())
    if sorted(tomb) == sorted(tomb2):
        return True
    else:
        return False

def main():
    result = anagramm("listen","silent")
    print(result)
    result = anagramm("A gentleman","Elegant man")
    print(result)
    result = anagramm("Clint Eastwood","Old west action")
    print(result)
    result = anagramm("dormitory","dirty room ")
    print(result)
    print("###################")
    result = anagramm2("listen","silent")
    print(result)
    result = anagramm2("A gentleman","Elegant man")
    print(result)
    result = anagramm2("Clint Eastwood","Old west action")
    print(result)
    result = anagramm2("dormitory","dirty room ")
    print(result)
    

##############################################################################

if __name__ == "__main__":
    main()