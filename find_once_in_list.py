#!/usr/bin/env python
#n = int(raw_input('how many nubers? '))

l = raw_input().split(' ')
print l
m = [int(x) for x in l]
k = {}
for i in range(len(m)):
    
    if not k.has_key(m[i]):
        k[m[i]] = 1
    else:
        k[m[i]] += 1

#max = [0,0]
#print k.keys()
#for q in k.keys():
#    if k[q] > max[1]:
#        max[1] = k[q]
#        max[0] = q

for i in k.keys():
    if k[i] == 1:
        print i

        

