#!/usr/bin/env python3


def main():

    szoveg = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""
    ujszoveg = ""

    for i in range(len(szoveg)):
        if szoveg[i] == ' ' or szoveg[i] == '!' or  szoveg[i] == ':' or szoveg[i] == '.' or szoveg[i] == '?' or szoveg[i] == '\n':
            ujszoveg += szoveg[i]
        else:
            if ord(szoveg[i])+2 > 90 and ord(szoveg[i])+2 < 96:
                ujszoveg += chr(ord(szoveg[i])+2-26)
            else:
                if ord(szoveg[i])+2 > 122:
                    ujszoveg += chr(ord(szoveg[i])+2-26)
                else:
                    ujszoveg += chr(ord(szoveg[i])+2)

    print(ujszoveg.strip())
##############################################################################



if __name__ == "__main__":


    main()