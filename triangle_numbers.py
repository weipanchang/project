#!/usr/bin/env python

def triangle_number(n):
    if n ==0: return None
    if n ==1: return [1]
    if n ==2: return [1,1,1]
    else:
        l = [None] * ((n * 2) -1 )
        
        l[0] = triangle_number(n-1)[0]
        l[1] = triangle_number(n-1)[0] + triangle_number(n-1)[1]
        
        for i in xrange(2, ((n * 2) -1)/2 + 1):
            l[i] = triangle_number(n-1)[i-2] + triangle_number(n-1)[i-1] + triangle_number(n-1)[i]
        
        for i in xrange(len(l)-1, len(l) / 2  ,-1):
            
            l[i] = l[n * 2 -2 -i]
        
        return l

def main():
    
    print triangle_number(1)
    print triangle_number(2)
    print triangle_number(3)
    print triangle_number(4)
    print triangle_number(5)
    print triangle_number(6)

if __name__ == '__main__':
    main()