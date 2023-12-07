#array for sum of divisors
d = [1]*9999

#iterate over all factors smaller than 100000
for i in range(2,10000):
    #only looking for divisors that are smaller so 1*i = cur should not be included
    cur = 2*i
    #multipy until limit
    while cur < 10000:
        #there is an n>1 so that n*i = cur it follows that i is a divisor of cur 
        #cur-1 because array is 0 indexed
        d[cur-1] += i
        cur += i


sum = 0
#find amicable numbers and sum them up
for i in range(1,10000):
    #check if i is amicable number and add to sum
    if d[i-1] < 10000 and d[d[i-1]-1] == i and d[i-1]!=i :
        sum += i
print(sum)

