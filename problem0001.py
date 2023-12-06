n=1000
#variable to sum up all multiples of 3 and 5
res = 0 
#multiples of 3 
for i in range(3,n,3):
    #skip numbers that are also multiple of 5
    if not (i%5 == 0):
        res = res + i

for i in range(5,n,5):
    res = res + i


print(res)