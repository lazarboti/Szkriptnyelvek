#!/usr/bin/env python3

def main():
    f = open("string1.py", "r")
    to = open("string1_clean.py", "w")
    for line in f:
        line.replace("\n","")
        if(not (line.strip()).startswith("#")): 
           to.write(line) 
    to.close
    f.close

##############################################################################

if __name__ == "__main__":
    main()