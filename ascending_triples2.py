#!/usr/bin/env python

def ascending_triples(array):
    triples = set()

    array_size = len(array)

    for i in range(array_size - 3):
        for j in range(i + 1, array_size):
            for k in range(j + 1, array_size):
                x = array[i]
                y = array[j]
                z = array[k]

                if x < y < z:
                    triples.add((array[i]))

    return triples

def main():
    #n = int(raw_input())

    raw_array = raw_input().split(" ")
    print raw_array
    array = [int(i) for i in raw_array]
    print array
    triples = ascending_triples(array)
    #print len(triples)

if __name__ == "__main__":
    main()

"""
def assend(n, l):
    result = []
    for i in range(n - 3):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] < l[j]  and l[j] < l[k]:
                    if [l[i], l[j], l[k]] not in result:
                        result.append([l[i], l[j], l[k]])
    return result

def main():
    n = int(raw_input())
    l1 = raw_input().split(" ")
#    print n, l1
    l2 = []
    for i in range(len(l1)):
        l2.append(int(l1[i]))
#    print l2
    print assend(n, l2)
    return

if __name__ ==  "__main__":
    main()
"""
