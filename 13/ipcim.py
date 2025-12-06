#!/usr/bin/env python3

import json
import requests

def main():
    url = requests.get("http://ipinfo.io/")

    f = url.json()
    print("Az ön ip cime: {0}".format(f["ip"]))


##############################################################################

if __name__ == "__main__":
    main()