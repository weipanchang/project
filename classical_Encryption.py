#!/usr/bin/env python
import math
def do_string_encrpt(st1):
    s = ''.join(st1.split(' '))

    s_len=len(s)
    
    if math.ceil(math.sqrt(s_len)) * math.floor(math.sqrt(s_len)) >= s_len: #defin column, raw
        c, r  = math.ceil(math.sqrt(s_len)), math.floor(math.sqrt(s_len))
    else:
        c, r = math.ceil(math.sqrt(s_len)), math.ceil(math.sqrt(s_len))
    c, r = int(c), int(r)
#    print c, r

    l = [] #slice string to each raw
    for i in range(r):
        l.append(s[i * c : (i + 1) * c])
    l [-1] = l[-1].ljust(c, ' ')

    k = []  #split earch element in the row list to single character
    for i in l:
        k.append([ch for ch in i])
#    print k
    m = zip(*k) # transpose
#    print m
    x = []
    for i in m:
        x.append([''.join(i)]) #put each element back to string
#    print x
    for i in x:
        print i[0]


def main():
    do_string_encrpt('if man was meant to stay on the ground god would have given us roots 123')


if __name__ == '__main__':
    
    main()