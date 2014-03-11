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
    factor = [x  for x in range(2,n+1) if number % x == 0]

    return sorted(factor)

def do_primary(l):
    m = []
    for i in l:
        n = int(math.sqrt(i))
        is_primary = True
        if i == 3 or i == 2:
            m.append(i)
            continue
        if i % 2 == 0:
            continue
        for j in range(3, n + 1):
            if (i % j == 0):
                is_primary = False
                break
        if is_primary == True:
            m.append(i)
    return m

#def is_prime(number):
#    if number > 1:
#        if number == 2:
#            return True
#        if number % 2 == 0:
#            return False
#        for current in range(3, int(math.sqrt(number) + 1), 2):
#            if number % current == 0: 
#                return False
#        return True
#    return False

def do_multiplicities(number, l):
    #n = []
    #for i in l:
    #    n.append(multiplicity(number, i))
    return [multiplicity(number, i) for i in l ]

#def multiplicity(n, p):
    #i = 0
    #while not n % p:
    #    i, n = i+1, n/p
    #return i

def multiplicity(n, p):

    def recurse_multiplicity(i, n):
        return i if n % p else recurse_multiplicity(i + 1, n / p)
    return recurse_multiplicity(0, n)

def main():
    number_input = int(raw_input("what is the number? "))
    number = do_factorial(number_input)

    factor_list = do_factor(number)
#    print factor_list
    primary_list = do_primary(factor_list)
#    print primary_list
    multiplicities_list = do_multiplicities(number, primary_list)

    answer = 1
    for i in multiplicities_list:
        answer = answer * (i+1)
    print answer

if __name__ == '__main__':
    main()
