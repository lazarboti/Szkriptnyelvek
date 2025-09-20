#!/usr/bin/env python3

def palindrom(s1):
    s2 = s1
    s2 = s2[::-1]
    if s1.lower() == s2.lower():
        print("A szó polindróm")
    else:
        print("A szó nem polindróm")

def main():
    palindrom("Abba")

##############################################################################

if __name__ == "__main__":
    main()
