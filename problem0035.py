from primesieve import Iterator

#function to generate all rotations of a list
def rotations(arr):
    res = [] 
    for i in range(0, len(arr)):
        #append from current index to end and append from start to current index
        res.append(arr[i:len(arr)] + arr[0:i])
    return res

#dict for prime look-up in O(1)
primecheck ={}
prime_it = Iterator()

#calculate primes up to 1 million and create lookup table
while (prime_n := prime_it.next_prime()) < 10**6:
    primecheck[prime_n] = True

count = 0

#check for all primes
for prime in primecheck.keys():
    #assume all rotations are prime
    allPrime = True
    #iterate over all rotations of current prime
    for rotation in rotations(str(prime)):
        #found a rotation that isn't prime
        if not int(rotation) in primecheck.keys():
            #set allPrime Flag to False and skip remaining rotations
            allPrime = False
            break
    if allPrime:
        count += 1 

print(count)
