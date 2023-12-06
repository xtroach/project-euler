#since the smallest common multiple of 19 and 20 is 380 we can iterate in steps of 380
#TODO: solution with analtyical result of all least common multiple probably faster
cur_nr = 380
while True:  
    divisable_by_all = True
    #check if cur_nr is divisable by all
    for i in range(20,0,-1):
        #if cur_nr is not divisible by i we can stop checking if it's divisiable by the other numbers
        if (cur_nr%i != 0):
            divisable_by_all = False
            break
    #if divisiable_by_all is True at this point we found the smalles nr that is diviable by all
    if divisable_by_all:
        break
    #iterate in steps of 380 since it's the lcm of 19 and 20
    cur_nr = cur_nr + 380

print(cur_nr)