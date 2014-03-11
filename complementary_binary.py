#!/usr/bin/env python

import math

    
def decimal_to_binary(n):
    i = 0
    while math.pow(2, i) <= n:
        i += 1
    i -= 1

    binary_string = ""
    accumulator = n
    for k in range(i, -1, -1):
        power = int(math.pow(2, k))

        if power <= accumulator:
            accumulator -= power
            binary_string += "1"
        else:
            binary_string += "0"
    return binary_string
    
def binary_to_decimal(b):
    accumulator = 0
    
    for k, n in enumerate(b[::-1]):
        #print k, n
        accumulator += math.pow(2, k) * int(n)
    
    return int(accumulator)
    
def complement_binary(b):
    print b
    print  ''.join(["1" if c == "0" else "0" for c in b])
    return ''.join(["1" if c == "0" else "0" for c in b])
    
    
def getIntegerComplement(n):
    return binary_to_decimal(complement_binary(decimal_to_binary(n)))


print getIntegerComplement(14)