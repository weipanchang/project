#!/usr/bin/env python

import sys
        
def remove_dup():
    s = set()
    while 1:
        n = raw_input('input number \n')
        if int(n) in s:
            print n
        s.add(int(n))
    
    

remove_dup()
        