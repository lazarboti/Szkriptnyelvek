#!/usr/bin/env python3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n- 1):
        if n % i == 0:
            return False
    return True


# Prímszámok keresése 1-től indulva


def main():
    N = 20  # ennyi prímszámot keresünk
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

##############################################################################

if __name__ == "__main__":
    main()