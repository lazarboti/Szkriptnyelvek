#!/usr/bin/env python3


def main():
    borton = [0] * 600

    for i in range(1, 601):
        for j in range(0, 600, i):
            borton[j] = 1 - borton[j]  

   
    for i in range(0, 600): 
        if borton[i] == 1:
            print(i,end="")



##############################################################################

if __name__ == "__main__":
    main()