#!/usr/bin/env python

def increment_version(version, i):
    index = int(i)
    tokens = [int(c) for c in version.split(".")]
    tokens[index] += 1

    for i in range(index + 1, len(tokens)):
        tokens[i] = 0

    return ".".join([str(c) for c in tokens])
i = raw_input()
version, index = i.split(' ')

print increment_version(version,index)