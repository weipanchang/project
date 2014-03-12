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

    return recursive(n, int(math.log(n,2)))
    

def complementary(s):
    return ''.join(['1' if c == '0' else '0' for c in s] )

def binary_to_decimal(s):
# s is visble under recursive
    def recursive( i):
        if i == len(s) - 1:
            return int(s[i]) * int(math.pow(2, len(s)- i -1))
        else:
            result = int(s[i]) * int(math.pow(2, len(s)- i - 1))
            return result + recursive(  i + 1)
    return recursive(0)

#print decimal_to_binary(16)
#print complementary('1101')
#print binary_to_decimal('0001')
print binary_to_decimal(complementary(decimal_to_binary(50)))