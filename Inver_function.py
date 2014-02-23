#!/usr/bin/env python
def multiple(a,b):
    return a * b

def multiple_2(a,b):
    return a * b


def add(a,b): 
    return a + b

def add_and_5(a,b): 
    return a + b + 5


def do_invert_func(f,z):
    l = []
    m = [(a,b) for a in range(z) for b in range(z)]
    for (x,y) in m:
        if f(x,y) == z:
            l.append((x,y))
    return l

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

