#!/usr/bin/env python3

def tisztit(input):

    return input.replace(' ', '').replace('\n', '').replace('\t', '')

def main():
    
    eredeti= "192.20.246.138:\n 6666"
    print(f"Eredeti sztring: {eredeti}")
    tiszta = tisztit(eredeti)
    print(f"Tisztított sztring: '{tiszta}'")

##############################################################################

if __name__ == "__main__":
    main()
