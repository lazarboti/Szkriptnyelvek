#!/usr/bin/env python3

def hamming(input1:str, input2:str) -> int:
    result = 0
    if len(input1) != len(input2):
        result = -1
        return result
    else:
        for i in range(len(input1)):
            if input1[i] != input2[i]:
                result += 1
        return result


