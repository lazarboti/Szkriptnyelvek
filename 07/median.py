#!/usr/bin/env python3


def test(tomb):
    tomb  = sorted(tomb)
    if len(tomb) %2 == 1:
        return tomb[(len(tomb))//2]
    else:
        return (tomb[len(tomb)//2-1] + tomb[(len(tomb)//2)])/2

def main():
    result = test([1, 2, 3, 4, 5]) == 3
    print(result)
    result = test([3, 1, 2, 5, 3]) == 3
    print(result)
    result = test([1, 300, 2, 200, 1]) == 2
    print(result)
    result = test([3, 6, 20, 99, 10, 15]) == 12.5
    print(result)

##############################################################################

if __name__ == "__main__":
    main()