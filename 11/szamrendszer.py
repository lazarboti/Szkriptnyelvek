#!/usr/bin/env python3

def main() -> None:
    result = 0
    for n in range(1_000_000):
        binaris = bin(n)[2:]
        if str(binaris) == str(binaris[::-1]) and str(n) == str(n)[::-1] and  not str(n).startswith('0') and  not str(binaris).startswith('0'):
            result += n

    print(result)

##############################################################################

if __name__ == "__main__":
    main()