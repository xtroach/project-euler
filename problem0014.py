class CollatzChain:
    #lookup table for known chain lengths
    sequence_length = dict()

    def calculate_sequence_length(n):
        cur_length = 0
        cur = n
        while (cur != 1):
            #if the remainder of the chain is known add the length of that chain to length of the chain up to this oint
            if cur in CollatzChain.sequence_length.keys():
                cur_length = cur_length + CollatzChain.sequence_length[cur]
                #early return
                break

            #calculate next number in chain
            if cur%2 == 0:
                cur = int(cur/2)
            else:
                cur = 3*cur+1

            #increase length by 1
            cur_length = cur_length + 1
        #set lookup table for sequence started at n
        CollatzChain.sequence_length[n] = cur_length
        #return length
        return cur_length



max_length = 10
max_nr = 13
for i in range(1,10**6):
    #get length of collatz chain
    cur_length = CollatzChain.calculate_sequence_length(i)
    #if new maximum remember number the maximum was reached by
    if cur_length > max_length:
        max_length = cur_length
        max_nr = i 

#print result
print(max_nr)