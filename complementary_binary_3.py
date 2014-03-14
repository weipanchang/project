#!/usr/bin/env python

import math

def decimal_to_binary(n, base):
    l = [int(math.pow(base, i)) for i in range(int(math.log(n, 2)), -1, -1)]

    def recursive(n, i):
        
        if i ==  len(l)-1:
            return str(n)
        else:
            if n >= l[i]:
                x = str(n // l[i])
                n -=  n % (n // l[i])
                
            else: x = '0'
            return x + (recursive(n, i + 1))

    return recursive(n, 0)
    

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

print decimal_to_binary(14, 4)
#print complementary('1110')
#print binary_to_decimal('0001')
#print binary_to_decimal(decimal_to_binary(50))