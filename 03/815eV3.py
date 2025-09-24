#!/usr/bin/env python3

def palindrom(s1, i = 0):
    hossz = len(s1)

    if i >= hossz // 2:
        return True

    if s1[i].lower() != s1[hossz - i - 1].lower():
        return False
    
    
    return palindrom(s1, i + 1)

def main():
    
    if palindrom("Abbas"):
        print("A szó palindróm")
    else:
        print("A szó nem palindróm")

##############################################################################

if __name__ == "__main__":
    main()
