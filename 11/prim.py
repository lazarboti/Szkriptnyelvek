#!/usr/bin/env python3

MAX = 3000000

def test(start: int) -> int:
    for n in range(start, MAX):
        prim = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prim = False
                break
        if prim and str(n) == str(n)[::-1]:
            return n
    
    return 1

def main() -> None:
    print(test(31) == 101)
    print(test(130) == 131)
    print(test(131) == 131)
    print(test(10301) == 10301)


##############################################################################

if __name__ == "__main__":
    main()