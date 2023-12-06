import time
start_time = time.time()
#copy of string
num_str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#initialize max_product to low value
max_product = 0
#variable to store product of previous product, this allows the use of sliding window (diving by number that is not in window anymore, multiplying by number that is)
last_product = 0
#start index in nr string
i=0
#iterate over nr string
while(i<len(num_str)-12):
    #initialize empty array for nrs in current window
    nums = []
    #variable to track if current window contains a 0
    new_start = 0
    #start from the back so we find the latest occurence of a 0 first
    for j in range(12,-1,-1):
        #convert num
        num = int(num_str[i+j])
        #we found a 0
        if num == 0:
            #we can move our window to start past the last known occurence of a 0
            new_start = j+1
            break
        nums.append(num)
    #we can skip
    if new_start:
        #set index to start behind latest known occurence of a 0 
        i = i+new_start
        #we can't use sliding window until we recalclated product of window at new starting position
        last_product = 0
        continue

    product = 1
    #we didn't have to skip around and can use sliding window
    if last_product:
        #divide last known product by number that is not in the window anymore
        product = last_product/int(num_str[i-1])
        #multiply by number that is in window now
        product = product*int(num_str[i+12])
    else:
        #calculate product from scratch
        for factor in nums:
            if factor == 0:
                break
            product = product*factor
    #set max_product to maximum
    max_product = max(max_product,product)
    #we have a know product until we skip
    last_product = product
    i = i+1
#print result
print(max_product)
#print elapsed time
print(time.time() - start_time)