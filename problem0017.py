numbers = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tenths = ['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']



def get_characters_in_nr(n):
    #if number is bigg than one hundred
    if n>=100:
        #get right number prefix
        res = len(numbers[int(n/100)-1])
        #add 7 for 'hundred'
        res = res + 7
        #if nothing comes after
        if n%100 == 0:
            return res
        else:
            #add 3 for 'and' and calculate length of remainder
            return res + 3+  get_characters_in_nr(n%100)
    #numbers below 20 are special
    if n<20:
        return len(numbers[n-1])
    if n>=20:
        #get prefix from array
        res = len(tenths[int(n/10)-1])
        #if nothing comes after the tenths place
        if n%10 == 0:
            return res
        else:
            #add the length of remainder (single digit)
            return res + get_characters_in_nr(n%10)



#start with 11 for 'onethousand'
sum = 11
#sum up for all numbers
for i in range(1,1000):
    sum = sum + get_characters_in_nr(i)

print(sum)


