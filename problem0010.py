from primesieve import Iterator

prime_it = Iterator()
sum = 0 
#assign next prime and check if it is smaller than 2 million
while((prime := prime_it.next_prime()) < 2*10**6):
    #add to sum
    sum = sum + prime
#print sum
print(sum)
