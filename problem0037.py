from primesieve import Iterator

prime_it = Iterator()
prime_check = {}
found_numbers = []
while (prime := prime_it.next_prime()) <= 7:
    prime_check[prime] = True

while len(found_numbers) < 11:
    prime = prime_it.next_prime()
    prime_check[prime] = True
    truncable = True
    prime_str = str(prime)
    for i in range(1,len(prime_str)):
        lefttrunc = prime_str[i::] 
        if not int(lefttrunc) in prime_check.keys():
            truncable = False 
            break
        righttrunc = prime_str[:-i:] 
        if not int(righttrunc) in prime_check.keys():
            truncable = False
            break

    if truncable:
        found_numbers.append(prime)
        
print(sum(found_numbers))