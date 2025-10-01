#!/usr/bin/env python3


def main():

    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pff"]
    for szo in words:
        mely = 0
        magas = 0
        for betu in szo:
            if betu in MELY_MGHK:
                mely += 1
            elif betu in MAGAS_MGHK:
                magas += 1
        if magas > 0 and mely > 0:
            print("{} -> vegyes".format(szo))
            continue
        if magas == 0 and mely == 0:
            print("{} -> semmilyen".format(szo))
            continue
        if magas  > 0:
            print("{} -> magas".format(szo))
            continue
        if mely  > 0:
            print("{} -> mely".format(szo))
            continue

##############################################################################



if __name__ == "__main__":


    main()