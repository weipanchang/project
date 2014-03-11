#!/usr/bin/python
#author: william
#date:
#purpose
import math

def do_factorial(n):
    if n == 1: return 1
    else: return n * do_factorial(n-1)

def do_factor(number):
    n = int((math.sqrt((number))) + 1)
#    n = number + 1    
    factor=[]
    
    for i in range(2,n):
        if (number%(i) == 0):
           if i not in factor:
               factor.append(i)
           if number/i not in factor:
               factor.append(number/i)
    return sorted(factor)

def do_primary(l):
    m = []
    for i in l:
        n = int(math.sqrt(i))
        is_primary = True
        for j in range(2, n + 1):
            if (i%j == 0):
                is_primary = False
                break
        if is_primary == True:
            m.append(i)
    return m

def do_multiplicities(number, l):
    n = []
    for i in l:
        n.append(multiplicity(number, i))
    return n

def multiplicity(n, p):
    i = 0
    while not n % p:
        i, n = i+1, n/p
    return i

def main():
    number_input = int(raw_input("what is the number? "))
    number = do_factorial(number_input)
#    print number
    factor_list = do_factor(number)
#    print factor_list
    primary_list = do_primary(factor_list)
#    print primary_list
    multiplicities_list = do_multiplicities(number, primary_list)
#    print multiplicities_list
    answer = 1
    for i in multiplicities_list:
        answer = answer * (i+1)
    print answer

if __name__ == '__main__':
    main()
