#dictionary that denotes if chain sequence of key ends in 1 or 89
chain_dict = {1: 1,  89: 89}

#count of chains that end in 89
eighty_nine_count = 0


for i in range(1,10**7):
    #start with i
    cur = i 
    #keep continuing the sequence until we find number that we know if it ends in 89
    while cur not in chain_dict.keys():
        cur = sum([int(c)**2 for c in str(cur)])

    #make new entry for i to remember if it ends in 1 or 89
    chain_dict[i] = chain_dict[cur]
    #if it ends in 89 increase the count
    if chain_dict[cur] == 89:
        eighty_nine_count += 1
#print count
print(eighty_nine_count)