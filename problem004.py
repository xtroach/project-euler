#initialize max to low value
max_product = -1 

#start with largest 3-digit number (999) and count down to smallest (100)
for i in range(999,99,-1):
    #set second factor to i
    j = i 
    #count down j while j*i is still bigger than the laregest palindrome number already found
    #assign j*i to product so we don't have to calculate j*i multiple times
    while ((product := j*i) >= max_product):
        
        product_str = str(product)
        #check if current product is palindrom
        if product_str == product_str[::-1]:
            #assign new maximum palindrom
            max_product = product
        j = j-1    
#print result
print(max_product)