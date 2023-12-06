#upper bound of fibonacci term
upper_bound = 4 * 10 ** 6 # 4 million
#variable to sum up even terms start with 2 
res = 2 

#fibonacci terms / start of sequence
last_fibs = [1,2]

i = 0 
while True:
    #calclate next term in sequence
    next_fib = sum(last_fibs)
    #break if term exceeds upper bound
    if next_fib > upper_bound:
        break
    #add to result if term is even TODO: skipable Iterations?
    if not (next_fib%2):
        res = res + next_fib
    #store new most recent fibonacci term in array (alternatingly on index 0 and 1)
    last_fibs[i] = next_fib
    i = (i+1)%2
print(res)