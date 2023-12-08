from itertools import permutations

#generate permutations
perms = permutations([str(i) for i in range(0,10)])
#concat them from tuples to strings
perms = [''.join(perm) for perm in perms]
#sort 
perms.sort()
#return millionthed term (0 indexed)
print(perms[10**6-1])

#TODO: do permutations manually