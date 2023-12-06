from primesieve import Iterator as PrimeIterator 
n = 10001
#instantiate primeiterator 
prime_it = PrimeIterator()
#iterate to n-th prime
for i in range(0,n):
    prime = prime_it.next_prime()
#print prime
print(prime)