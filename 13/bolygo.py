#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        for line in f:
            tomb=line.split(",")
            szo = tomb[0].lower()
            if  "j" in szo and "s" in szo and "u"  in szo and "n" in szo:
                if szo.index("j") <  szo.index("s") < szo.index("u") < szo.index("n"):
                    print(szo)

##############################################################################

if __name__ == "__main__":
    main()