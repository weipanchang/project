#!/usr/bin/env python

def do_tails(l): #O(n)
    if len(l) <= 2: return [l[-1:]]
    else:
        return [l[1:]] + do_tails(l[1:])
    
def do_string_compare(l,m): #O(n)
    if len(l) == 0 and len(m) == 0: return "l = m"
    if len(l) == 0  : return "l < m"
    if len(m) == 0  : return "l > m"
    else:
        if l[0] > m[0]: return 'l > m'
        if l[0] < m[0]: return 'l < m'
        return do_string_compare(l[1:],m[1:])

def do_smallest_tail(s):
    
    return


def tails():
    print do_tails([3, 3, 4]), "should be [[3,4], [4]]"
    print do_tails([3, 3, 4, 5, 6]), "should be [[3, 4, 5, 6], [4, 5, 6], [5, 6], [6]]"
    print do_tails("hello"), "should be ['ello', 'llo', 'lo', 'o']"
    return

def string_compare():
    print do_string_compare('abcd', 'bbc'), " 'abcd', 'bbc' should be l < m"
    print do_string_compare('bcdd', 'abc'), " 'bcdd', 'abc')should bel > m"
    print do_string_compare('', 'abc'), " '', 'abc' should be l < m"
    print do_string_compare('abcd', 'abc'), " 'abcd', 'abc' should be l > m"
    print do_string_compare('b', 'abc'), " 'b', 'abc' should be l > m"
    print do_string_compare('abc', 'abc'), " 'abc', 'abc' should be l = m"
    return

def smallest_tail():
    print do_smallest_tail('earls'), " 'earls' should be 'arls' "
    return


if __name__ ==  "__main__":
    print "\n do tails"
    tails()
    print "\n\n string compare"
    string_compare()
    print "\n\n smallest tail"
    smallest_tail()