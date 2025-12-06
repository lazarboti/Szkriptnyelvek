#!/usr/bin/env python3

import random

def shuffled(tomb):
    result = tomb[:]
    random.shuffle(result)
    return result

def main():
    tomb = [1,2,3,4,5,6,7,8,9,10]
    result = shuffled(tomb)
    print("Eredeti tömb: {0}".format(tomb))
    print("Kevert tömb: {0}".format(result))


##############################################################################

if __name__ == "__main__":
    main()