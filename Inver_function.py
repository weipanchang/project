#!/usr/bin/env python
def multiple(a,b):
    return a * b

def multiple_2(a,b):
    return a * b * 2


def add(a,b): 
    return a + b

def add_and_5(a,b): 
    return a + b + 5


def do_invert_func(f,z):
    m = [(a,b) for a in range(z) for b in range(z) if f(a,b) ==z]
    return m

def main():
    print do_invert_func(multiple, 40)
    print ""
    print do_invert_func(multiple_2, 40)
    print ""
    print do_invert_func(add, 40)
    print ""
    print do_invert_func(add_and_5, 40)
    return

if __name__ ==  "__main__":
    main()

