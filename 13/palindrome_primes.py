#!/usr/bin/env python3

import json

def main():
    with open("primes.json", "r") as f:
        data =   json.load(f)
    
    result = 0
    for e in data['primes']:
        s = str(e)
        if s == s[::-1]:
            result +=1
    
    print(result)

##############################################################################

if __name__ == "__main__":
    main()