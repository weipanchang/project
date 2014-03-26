#!/usr/bin/env python

import sys

def student_last_name(student_record):

    last_name_set = {x for x in student_record.values[0]}
    return list(last_name_set)


def average_gpa(student_record):

    list_gpa = [n for n in student_record.values[2]]
    return sum(list_gpa) / len(student_record)

def read_file(s):
    record = {}

    try:
        with open(s, 'r') as infile:
            
            for line in infile:
                field = line.split()
                id, lastName, firstName, gpa = int(field[0]), field[1], field[2], float(field[3])
                record[id] = [lastName, firstName, gpa]   
        return record
    except IOError:
        #print "The file does not exist, exiting gracefully"
        sys.exit("The file %s does not exist, exiting gracefully" % s)


def main(s):
    student_record = read_file(s)
    
    print average_gpa(student_record)
    for i in student_last_name(student_record):
        print i,


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        
        sys.exit("Usage: python %s [input file path]" % sys.argv[0])
           
    read_in_file_name = sys.argv[1]
    main(read_in_file_name)