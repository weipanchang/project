#!/usr/bin/env python
import math

def func_gen(n):
    
    for i in range(n):
        is_primary = True
        if i % 2 == 0: is_primary = False
        for n in xrange(3, int(math.sqrt(i))+1,2):
            if i % n == 0:
                is_primary = False
                break
        if is_primary == True:
            yield i
    return


def main():
    mylist = func_gen(16)
    for i in mylist:
        print i
    return

if __name__ == '__main__':
    main()

