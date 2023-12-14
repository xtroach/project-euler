from primesieve import primes 

#only demoninators that are not a prime factor of 10 (all primes except 2 and 5) will produce reoccuring cycles
p =  primes(1000)

#keep track of which denominator produced longest reoccuring cycle
max_len = 0
max_val = 0 
for prime in p:
    remainder = 1
    seen = {}
    pos = 0
    while True:
        pos += 1
        #calculate digit at current position
        remainder = (remainder*10)%prime
        #if digit has occured before
        if remainder in seen.keys():
            #distance between current position and the last time digit was seen
            length = pos - seen[remainder]
            if length > max_len:
                max_val = prime 
                max_len = length
            break
        #remember where digit first occured
        seen[remainder] = pos
print(max_val)