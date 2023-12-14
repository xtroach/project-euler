from primesieve import Iterator

isPrime = {}

largest = 39
max_a = 1
max_b = 41
calced_primes = []
primes_it = Iterator()
#calculate biggest prime we need to know
while True:
    next_prime = primes_it.next_prime()
    calced_primes.append(next_prime)
    isPrime[next_prime] = True
    if calced_primes[-1] >= largest**2+ max_a*largest +max_b:
        break

#iterate over all a-s and b-s
for a in range(999,-1000,-1):
    for b in range(-1000,1001):

        n = largest
        #check if all terms up to largest n are prime
        while (res := n**2 + a*n + b) in isPrime.keys() and n>0:
            n -= 1
        #skip if not
        if n != 0:
            continue
        n = largest + 1 


        #generate primes in case limit is exceeded
        while n**2 + a*n+b > calced_primes[-1]:
            next_prime = primes_it.next_prime()
            calced_primes.append(next_prime)
            isPrime[next_prime] = True

        #increase n while following terms are prime
        while (res := n**2 + a*n + b) in isPrime.keys():
            n += 1
            #generate more primes if needed
            while n**2 + a*n+b > calced_primes[-1]:
                next_prime = primes_it.next_prime()
                calced_primes.append(next_prime)
                isPrime[next_prime] = True
        largest = n
        max_a = a
        max_b = b

print(max_a*max_b)