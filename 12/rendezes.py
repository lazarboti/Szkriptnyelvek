#!/usr/bin/env python3

def main():
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (121, 'Wyoming', 'NY', 8722),
    (3, 'Allegany', 'NY', 11986),
    (123, 'Yates', 'NY', 5094)
]
    result1=sorted(data, key= lambda t : t[-1])
    print(result1)

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    result2=sorted(users, key= lambda t : int(t.split(":")[0]))
    print(result2)

    matrix = [ [2, 6], [1, 3], [5, 4] ]
    result3=sorted(matrix, key= lambda m : m[1])
    print(result3)

##############################################################################

if __name__ == "__main__":
    main()