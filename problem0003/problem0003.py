import primesieve

#we will be divididing our input by primes and remember the quotient
quotient=600851475143
#initializing prime for scoping
prime = 0

#while the quotient still can be factorized
while quotient != 1:

    #generate iterator for primes (save memory)
    prime_iteratior = primesieve.Iterator()

    #start with smalles prime (2)
    prime = prime_iteratior.next_prime()

    #condition for readability if prime==quotient, loop always breaks and quotient always is 1
    #so wrapping loop doesn't do another iteration either
    while prime <= quotient:
        #if the quotient can be evenly divided by the current prime => prime is a prime factor of our number
        if quotient%prime == 0:
            #set quotient for next iteration
            quotient = quotient/prime
            #start over with 2 
            break
        #continue with next prime
        prime = prime_iteratior.next_prime()
#since we start with the smallest prime largest prime factor wil be always in last step
print(prime)


