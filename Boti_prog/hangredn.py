#!/usr/bin/env python3
from enum import Enum, auto

class Hangrend(Enum):
    MAGAS = auto()
    MELY = auto()
    VEGYES = auto()
    SEMMI = auto()

def besorolas(szo):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    mely = sum(b in MELY_MGHK for b in szo)
    magas = sum(b in MAGAS_MGHK for b in szo)
    if mely > 0 and magas > 0:
        return Hangrend.VEGYES
    if mely == 0 and magas == 0:
        return Hangrend.SEMMI
    if magas > 0:
        return Hangrend.MAGAS
    return Hangrend.MELY

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pff"]
    for szo in words:
        print(f"{szo} -> {besorolas(szo).name.lower()}")

if __name__ == "__main__":
    main()
