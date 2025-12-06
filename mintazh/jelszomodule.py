import random


def general_jelszo(hossz):

    kis = "abcdefghijklmnopqrstuvwxyz"
    #nagy = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    szam = "0123456789"
    result = ""
    for i in range(hossz):
        f = random.randrange(2)
        if (f == 0):
            r = random.choice(kis)
            result += r
        else:
            r = random.choice(szam)
            result += r

    return result

