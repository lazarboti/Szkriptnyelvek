#!/usr/bin/env python3

def fordit(c):
    if(c == "["):
        return "]"
    elif(c == "{"):
        return "}"
    elif(c == "("):
        return ")"

def zaro(input):
    verem = []
    for c in input:
        if(c == "(" or c == "[" or c == "{"):
            verem.append(c) 
        if(c == ")" or c == "]" or c == "}"):
            last = verem.pop()
            last = fordit(last)
            if( c != last):
                return False
    if(len(verem) == 0):
        return True
    else:
        return False

def main():
    print(zaro("((5+3)*2+1)"))
    print(zaro("{[(3+1)+2]+}"))
    print(zaro("(3+{1-1)}"))
    print(zaro("[1+1]+(2*2)-{3/3}"))
    print(zaro("(({[(((1)-2)+3)-3]/3}-3)"))

##############################################################################

if __name__ == "__main__":
    main()