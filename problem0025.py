#array to cache last two terms in fibonacci sequnce
last_fibs = [1,1]
#we know first two terms so we start with 3rd term
i = 3 
while True:     
    #calculate next (i-th) term of sequence (store them alternatingly in at first and last positon) 
    last_fibs[i%2] = last_fibs[i%2] + last_fibs[(i+1)%2]   
    #if term has more than 1000 digits were done
    if len(str(last_fibs[i%2])) == 1000:
        break
    #increase index 
    i += 1
print(i)