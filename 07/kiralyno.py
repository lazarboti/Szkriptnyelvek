#!/usr/bin/env python3


def sakk(tomb):
    szamlalo = 7
    print("+-----------------+")
    for i in range(8):
        print("| ", end="")
        if szamlalo in tomb:
            ind = tomb.index(szamlalo)  
        else:
            ind = -1
        for j in range(8):
            if j == ind:
                print("Q ", end="")
            else:
                print(". ", end="")
        szamlalo -=1


        print("|")

    print("+-----------------+")

def main():
    sakk([0,4,7,5,2,6,1,3])

##############################################################################

if __name__ == "__main__":
    main()