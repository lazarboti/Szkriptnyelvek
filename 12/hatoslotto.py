#!/usr/bin/env python3

def main():

    for a in range(1, 46):
        for b in range(a+1, 46):
            for c in range(b+1, 46):
                for d in range(c+1, 46):
                    for e in range(d+1, 46):
                        for f in range(e+1, 46):

                            
                            if a + b + c + d + e + f != 90:
                                continue

                            
                            if a * b * c * d * e * f == 996300:
                                print("Megoldás:", a, b, c, d, e, f)

##############################################################################

if __name__ == "__main__":
    main()