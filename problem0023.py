
#array for sum of divisors
d = [1]*28124

#iterate over all factors smaller than 100000
for i in range(2,28124):
    #only looking for divisors that are smaller so 1*i = cur should not be included
    cur = 2*i
    #multipy until limit
    while cur <= 28124:
        #there is an n>1 so that n*i = cur it follows that i is a divisor of cur 
        #cur-1 because array is 0 indexed
        d[cur-1] += i
        cur += i

#get abundant nrs
abundant_nrs = []
for i in range(1,28124):
    if d[i-1]>i:
        abundant_nrs.append(i)


# triangular number: n*n(+1)/2
sum_of_all = (28123*28124)/2

#array to check if nr that is the sum of two abundant nrs has already been included inthe sum
included_in_sum = [False]*28123

#the sum of all nrs that is the sum of two abundant numbers
abundant_sum_sum = 0 
#iterate over abundant numbers
for i in range(len(abundant_nrs)):
    #ordered -> can break
    if abundant_nrs[i] > 28123:
        break
    for j in range(i,len(abundant_nrs)):
        abundant_sum = abundant_nrs[i] + abundant_nrs[j]
        #if sum has already been included or we are past the limit where all numbers
        #can be expressed as sum of two abundant numbers
        if abundant_sum > 28123 or included_in_sum[abundant_sum-1]:
            continue
        #add term to sum and remember that this sum has already been included
        abundant_sum_sum += abundant_sum
        included_in_sum[abundant_sum-1] = True

#the difference between sum of all numbers up to 28123 
# minus the sum of all numbers that can be expressed as sum of two abundant numbers
# => the sum of all numbers who can not be expressed as sum of two abundant numbers
print(sum_of_all - abundant_sum_sum)