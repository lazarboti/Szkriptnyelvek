#!/usr/bin/env python3

from typing import List

def oldalak(input: str) -> List[int]:
    tomb = input.split(",")
    result = [] 
    for e in tomb:
            oldal = e.split("-")
            
            if len(oldal) == 2:
                for n in range(int(oldal[0]), int(oldal[1])+1):
                    result.append(int(n))
            else:
                 for n in oldal: # type: ignore
                    result.append(int(n))
                 

    return result

def main() -> None:
    print(oldalak("1-3,7,9,11-15"))
##############################################################################

if __name__ == "__main__":
    main()