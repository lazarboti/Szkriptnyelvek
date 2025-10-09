#!/usr/bin/env python3


def ex_1():
    words =['auto', 'villamos', 'metro']
    result = [word.upper() + "!" for word in words]
    print(result)

def ex_2():
    words = ['aladar', 'bela', 'cecil'] 
    result = [word.capitalize() for word in words]
    print(result)

def ex_3():
    numbers = [0 for n  in range(10)]
    print(numbers)

def ex_4():
    numbers = [n for n  in range(1 ,10+1)]
    numbers2 = [n*2 for n in numbers]
    print(numbers2)

def ex_5():
    tomb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
    result = [int(s)  for s in tomb]
    print(result)

def ex_6():  
    inp = "1234567"
    result = [int(c) for c in inp]
    print(result)

def ex_7():  
    inp = "The quick brown fox jumps over the lazy dog"
    result = [len(s) for s in inp.split()]
    print(result)

def ex_8():  
    inp = "python is an awesome language"
    result = [s[0] for s in inp.split()]
    print(result)

def ex_9():  
    inp = "The quick brown fox jumps over the lazy dog"
    result = [(s, len(s)) for s in inp.split()]
    print(result)

def ex_10():  
    result = [n for n in range(0,10,2)]
    print(result)

def ex_11():  
    result = [n*n for n in range(0,20,2)]
    print(result)

def ex_12():  
    result = [n*n for n in range(0,20,2) if str(n*n).endswith("4")]
    print(result)

def ex_13():  
    betuk = [chr(b) for b in range(65,91)]
    result = ''.join(betuk)
    print(result)

def ex_14():
    inp = [' apple ', ' banana ', ' kiwi']   
    result = [w.strip() for w in inp]
    print(result)

def ex_15():
    inp = [1, 0, 1, 1, 0, 1, 0, 0]   
    result = ''.join(str(n) for n in inp)
    print(result)



def main():
    ex_15()




##############################################################################

if __name__ == "__main__":
    main()