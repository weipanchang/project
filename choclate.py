#!/usr/bin/env python
#def get_choclate(m):
#    t = m.split(' ')
#    s = [int(x) for x in t]
#    n = s[0] // s[1]
#    m = n
#    #print m
#    #while m >= s[2]:
#    #    
#    #    k =  m // s[2]
#    #    m -= k * s[2]
#    #    n += k
#    #    m += k
#    def recursive(m):
#        if m < s[2]:
#            return 0
#        else:
#            k = m // s[2]
#            m -= k * s[2]
#            m += k
#            return k + recursive(m)
#    
#    return n + recursive(m)

def total_choclate(a, b):
    l = [0] * a
    for i in range(b):
        idx1, idx2, n = [int(x) for x in (raw_input('operation: ').split(' '))]
        for j in range(idx1-1, idx2):
            l[i] += n
        
    return sum(l)
    


#n = raw_input('number testcase? ')
a, b = raw_input('input? ').split(' ')
print total_choclate(int(a), int(b)) // int(a)
    


