#!/usr/bin/env python

def do_fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else:
        return do_fib(n-1) + do_fib(n-2)
    
for i in range(1,10):
    print do_fib(i)

n = int(raw_input('the number? '))

if n // 2 ==0 : print 'is not fib'
else:
    i = 0
    while 1:
        m = do_fib(i)
        if m > n:
            print 'is not fib'
            break
        elif n == m:
            print 'is_fib'
            break
        else:
            i += 1

