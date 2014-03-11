#!/usr/bin/env python

import math

def is_prime(n):
    if n == 1 or n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
        else: return True
    return

def main():
    
    n = int(raw_input("what is the number? "))
    #print n
    m = []
    l1 = [True] * (n )
    print l1
    for i in xrange(1, n+1):
        print i
        if l1[i-1] == False:
            continue
        if is_prime(i):
            for j in xrange(2, (n/i)):
                l1[j * i] = False
            m.append(i)
    print m



if __name__ == '__main__':
    main()