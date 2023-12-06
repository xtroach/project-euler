from primesieve import Iterator

class PrimeFactorLookUp:
    #look up table for known prime factorizations
    known_primes = dict()

    #function that returns prime factors of number n
    def prime_factors(n: int):

        quotient = n
        prime_factors = []
        #while quotient is not 1 it still can be factorized
        while quotient != 1:
            #prime nr factorization of remaining quotient is already in lookup table
            if quotient in PrimeFactorLookUp.known_primes.keys():
                #yield remaining factors
                for factor in PrimeFactorLookUp.known_primes[quotient]:
                    yield factor
                    prime_factors.append(factor)
                #early return
                break

            #because of early return this part only gets executed if prime nr factorization of remaining quotient isn't yet known
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
                    prime_factors.append(next_prime)
                    #start from lowest prime again 
                    break
        #remember prime factors for n in lookup table
        PrimeFactorLookUp.known_primes[n] = prime_factors

#for a nr with n prime factorization n = p_1**c_1 + p_2**c_2 + ... + p_m **c_m the number of divisors d(n) is
#d(n) = (c_1 + 1) * (c_2 + 1) + ... + (c_m + 1) see https://mathschallenge.net/library/number/number_of_divisors
def calc_nr_of_divisors_from_prime_factors(factors):
    res = 1
    i = 0 
    #iterate over factors (they are sorted in ascending order)
    while i < len(factors):
        cur_factor = factors[i]
        multiplier = 0
        #count occurences of same prime factor in prime nr factorization 
        while  i<len(factors) and cur_factor == factors[i]:
            multiplier = multiplier + 1
            i = i + 1
        #multipy by power of current prime factor + 1 e.g. (c_1 + 1)    
        res = res * (multiplier+1)
    return res

#generator function for triangle numbers
def triangle_nr_gen():
    i = 1 
    sum = 0 
    while True:
        sum = sum + i
        yield sum
        i = i + 1 

#iterate over triangle numbers
for triangle_nr in triangle_nr_gen():
    #get prime factors for current triangle number
    prime_factors = [factor for factor in PrimeFactorLookUp.prime_factors(triangle_nr)]
    #calculate number of divisors from prime number factorization
    nr_of_divisors = calc_nr_of_divisors_from_prime_factors(prime_factors)

    #if over 500 divisors we found the smalles triangle number that meets criteria
    if nr_of_divisors > 500:
        print(triangle_nr)
        break


