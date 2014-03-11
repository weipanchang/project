#!/usr/bin/env python

def assend(n, l):
    result = set()
    for i in range(n - 3):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] < l[j]  and l[j] < l[k]:
#                    if [l[i], l[j], l[k]] not in result:
                    result.add((l[i], l[j], l[k]))
    return result

def main():
    n = int(raw_input())
    l1 = raw_input().split(" ")
#    print n, l1
    #l2 = []
    #for i in range(len(l1)):
    #    l2.append(int(l1[i]))
    #
    print(assend(n, l1))
    
    #for i in result:
    #    n = n + 1
    #    print n, " ", i, "\n"
    #
    #return

if __name__ ==  "__main__":
    main()
