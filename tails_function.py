#!/usr/bin/env python

def do_tails(l): #O(n)
    if len(l) <= 2: return [l[-1:]]
    else:
        return [l[1:]] + do_tails(l[1:])
    
def do_string_compare(l,m): #O(n)
    if len(l) == 0 and len(m) == 0: return 0
    if len(l) == 0: return -1
    if len(m) == 0: return 1
    else:
        if l[0] > m[0]: return 1
        if l[0] < m[0]: return -1
        return do_string_compare(l[1:],m[1:])

def do_smallest_tail(s):  #O(n^2)
    t = do_tails(s)
    small = t[0]
    for i in t:
        if do_string_compare(small, i) == -1 : small = i
    return small       

def tails():
    print do_tails([3, 3, 4]), "should be [[3,4], [4]]"
    print do_tails([3, 3, 4, 5, 6]), "should be [[3, 4, 5, 6], [4, 5, 6], [5, 6], [6]]"
    print do_tails("hello"), "should be ['ello', 'llo', 'lo', 'o']"
    print do_tails('earls'), "should be ['arls', 'rls', 'ls', 's']"
    return

def string_compare():
    print do_string_compare('abcd', 'bbc'), " 'abcd', 'bbc' should be -1"
    print do_string_compare('bcdd', 'abc'), " 'bcdd', 'abc')should be 1"
    print do_string_compare('', 'abc'), " '', 'abc' should be -1"
    print do_string_compare('abcd', 'abc'), " 'abcd', 'abc' should be 1"
    print do_string_compare('b', 'abc'), " 'b', 'abc' should be 1"
    print do_string_compare('abc', 'abc'), " 'abc', 'abc' should be 0"
    return

def smallest_tail():
    print do_smallest_tail('earls'), " 'earls' should be 'arls' "
    print do_smallest_tail('edcba'), " 'edcba' should be 'a' "
    print do_smallest_tail('edcbaabcd'), " 'edcbaabcd' should be 'aabcd' "
    return


if __name__ ==  "__main__":
    print "\n do tails"
    tails()
    print "\n\n string compare"
    string_compare()
    print "\n\n smallest tail"
    smallest_tail()