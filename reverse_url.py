#!/usr/bin/env python

def reverse_label(s):
    tokens = s.split(".")
    
    prefix = tokens[0]
    suffix = "".join(tokens[2:])
    center = tokens[1]
    
    return suffix + '.' + center + '.' + prefix

def do_list(l):
    for i in l:
        print reverse_label(i)
        
do_list([www.nominum.com], [www2.sfo.example.com])