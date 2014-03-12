#!/usr/bin/env python

import math

def decimal_to_binary(n):

    def recursive(n, i):
        if i ==  0:
            return str(n)
        else:
            if n >= int(math.pow(2, i)):
                n -= int(math.pow(2, i))
                x = '1'
            else: x = '0'
            return x + (recursive(n, i - 1))
    
    #m = int(math.log(n,2))
    return recursive(n, int(math.log(n,2)))
    
    #return l
     
    #binary_string = ''   
    #l = []   
    #for i in range(m,-1,-1):
    #    if n >= int(math.pow(2, i)):
    #        l.append('1')
    #        n = n - int(math.pow(2, i))
    #    else:
    #        l.append('0')
    #
    #binary_string = ''.join(l)
    #return binary_string

def complementary(s):
    return ''.join(['1' if c == '0' else '0' for c in s] )

def binary_to_decimal(s):
    result = 0
    for i, j in enumerate(s[::-1]):
        result += math.pow(2,i) * int(j)
    return int(result)

print decimal_to_binary(16)
#print complementary('1101')
#print binary_to_decimal('0010')
print binary_to_decimal(complementary(decimal_to_binary(16)))