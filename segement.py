#!/usr/bin/env python


def smallest_segment(l):
    small_sum = l[0][:]
    for i in range(1, len(l)):
        if sum(l[i]) < sum(small_sum): small_sum = l[i][:]
    return small_sum
        


def segement_list(l):
    m = []
    for i in range(len(l)):
        for j in range(len(l) - i):
            m.append(l[j:j+i+1])
    return m

def main():
    print( [4, 2, 3]), " --->\n",  "segement_list of ( [4, 2, 3])", " should be [[4], [2], [3], [4, 2], [2, 3], [4, 2, 3]]"
    print "The smallest segment sum is " % (smallest_segment(segement_list([4, 2, 3])))
    #print segement_list( [-4, 2, 3, -2]), " should be [[4], [2], [3], [-2], [4, 2], [2, 3], [3, -2], [4, 2, 3], [2, 3, -2], [4, 2, 3, -2]]"
    #print "The smallest segment sum is " % (smallest_segment(segement_list([-4, -2, 3, 2])))
    return

if __name__ ==  "__main__":
    main()