#!/usr/bin/env python
def do_remove_dup(l):
    m = set()
    for i in l:
        m.add(i)
    return m

def get_int(l):
    for i in l:
        if i != "":
            #print i
            yield i

def main():
    l1 = raw_input("input the list: \n").split(" ")
    mylist = [int(x) for x in l1 if x != '']
    #mylist = get_int(l1)
    #print mylist
    #for i in mylist:
    #    print i
    print list(do_remove_dup(mylist))


if __name__ == '__main__':
    main()