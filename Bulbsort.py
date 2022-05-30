l = [6,5,4,3,2,1]

# for i in range(len(l) -1):
#     for j in range(len(l) - i -1):
#         if l [j] > l [j + 1]:
#             l[ j], l[j + 1] = l[j+1], l[j]
#     



def quicksort(l):
    if not l:
        return []
    else:
        return quicksort([a  for a in l if a < l[0] ]) + [l[0]] + quicksort([a for a in l if a > l[0] ])
    
print (quicksort(l))