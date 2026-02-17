def print_hi(name):
    print(f'Hi, {name}')

def szokoevek(ev1,ev2):
    eredmeny = []
    for n in range(ev1, ev2+1):
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            eredmeny.append(n)
    a
    return eredmeny


def palindrom (szam):
    return str(szam) == str(szam)[::-1]

def palindrom2 (szam):
    eredeti = szam
    forditott = 0
    while szam != 0:
        szj = szam % 10
        szam = szam // 10
        forditott = forditott*10 + szj

    return eredeti == forditott


def negyzetes(inp):
    eredmeny = []
    for n in inp:
        if n % 2 == 0:
            eredmeny.append(n**2)
    return eredmeny

def negyzetes2(inp):
    return  [n**2 for n in inp if n %2 == 0]




if __name__ == '__main__':
    print(szokoevek(1957, 2026))
    print(palindrom(1221))
    print(palindrom2(1231))
    print(negyzetes([1,2,3,4,5,6,7,8]))
    print(negyzetes2([1, 2, 3, 4, 5, 6, 7, 8]))
