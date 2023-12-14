#calculate binary representation
def get_binary_string(n):
    res = ''
    while (n>0):
        if n%2:
            res = '1' + res
        else:
            res = '0' + res
        n = int(n/2)
    
    return res



sum = 0
#since leading 0s are not allowed we can skip all even numbers since they always end with 0 in binary
for i in range(1,10**6,2):
    #get strings for both bases
    base_ten = str(i)
    base_two = get_binary_string(i)
    #if strings are equal forward and backward in both bases add i to the sum
    if base_ten[::-1] == base_ten and base_two[::-1] == base_two:
        sum += i

print(sum)