from primesieve import Iterator

#a generator function for prime factors of Number n in ascending order
def prime_factors(n: int):

    quotient = n
    #while quotient is not 1 it still can be factorized
    while quotient != 1:
        #start from lowest prime in every iteration 
        prime_it = Iterator()
        #iterate over primes up to the remaining quotient
        while (next_prime := prime_it.next_prime()) <= quotient:
            #if prime evenly divides quotient
            if (quotient%next_prime == 0):
                #set remaining quotient
                quotient = quotient/next_prime
                #next prime factor has been found
                yield next_prime
                #start from lowest prime again 
                break



print([i for i in prime_factors(15)])