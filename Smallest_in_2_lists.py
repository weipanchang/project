#!/usr/bin/env python
def do_pop(l,m):
    if len(l) ==0: return m.pop(0)
    if len(m) ==0: return l.pop(0)
    if l[0] > m[0]: return m.pop(0)
    return l.pop(0)


def do_find(l,m,k):   #O(k)
    for i in range(k):
        result = do_pop(l,m)
    return result

def main():
    print do_find( [3, 3, 4], [2, 7, 8], 1)
    print do_find( [3, 3, 4], [2, 7, 8], 2)
    print do_find([1,2,2,3,6,10,12,15], [2,2,3,4,7,7,8,8,8,9], 8)
    print do_find([1,2,2,3,6,10,12,15], [2,2,3,4,7,7,8,8,8,9], 16)
    print do_find([], [2,2,3,4,7,7,8,8,8,9], 4)
    
    return

if __name__ ==  "__main__":
    main()
    
