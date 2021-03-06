#!/usr/bin/env python


def smallest_segment(l): #O(N)
    small_sum = l[0]
    sum_value = sum(small_sum)
    for i in range(1, len(l)):
        if sum(l[i]) < sum_value:
            small_sum = l[i]
            sum_value = sum(small_sum)
    return small_sum

def segement_list(l): #O(N^2)
    m = []
    for i in range(len(l)):
        for j in range(len(l) - i):
            m.append(l[j:j+i+1])
    return m

def main():
    l = [4, 2, 3]
    print l, " -----> ", segement_list(l)
    print "smallest sum segment is ", smallest_segment(segement_list(l)), "\n"

    l = [-4, 2, -3, 3]
    print l, " -----> ", segement_list(l)
    print "smallest sum segment is ", smallest_segment(segement_list(l))

    l = [4, -4, -1, -3]
    print l, " -----> ", segement_list(l)
    print "smallest sum segment is ", smallest_segment(segement_list(l))
    return

if __name__ ==  "__main__":
    main()