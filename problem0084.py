import random
#copy paste field string
field_str = "GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3, JAIL, C1, U1, C2, C3, R2, D1, CC2, D2, D3, FP, E1, CH2, E2, E3, R3, F1, F2, U2, F3, G2J, G1, G2, CC3, G3, R4, CH3, H1, T2, H2"
#get field names in array
field_names = field_str.replace(" ","").split(",")
#dict to lookup indexes for field names
field_dict = {field_names[i]: i for i in range(40)}
#counter for doubles
doubles_counter = 0 
#number of sides of the dice
num_sides = 4
#how many rolls to simulate
iterations = 5*10**6

#function go get field index from 
def get_field_index(field_name):
    return field_dict[field_name]


#start on go 
pos = get_field_index("GO")

#build arrays for special field lookups
chances_indexes = [get_field_index("CH%d" % i ) for i in range(1,4)]
community_chest_indexes = [get_field_index("CC%d" % i ) for i in range(1,4)]
railway_indexes = [get_field_index("R%d" % i) for i in range(1,5)]
utility_indexes = [get_field_index("U%d"% i) for i in range (1,3)]

#return index of next railway station
def get_next_railway_index(pos):
    i=0
    #iterate so railway_indexes[i] is bigger than pos after iterations
    while i < len(railway_indexes) and pos >= railway_indexes[i]:
        i += 1     
    if i < len(railway_indexes):
        return railway_indexes[i]
    #there is no railwaystation left -> next round 
    else:
        return railway_indexes[0]

#return index of next utility plant see get_next_railway_index
def get_next_utility_index(pos):
    i=0 
    while i < len(utility_indexes) and pos >= utility_indexes[i]:
        i += 1
    if i < len(utility_indexes):
        return utility_indexes[i]
    else:
        return utility_indexes[0]    

#initialize empty array for visits
visits = [0 for _ in range(0,40)]

#function to take into account G2J, community chets and chance cards
def get_position_after_special(pos):

    #if the current position isn't G2J, a CC or CH square return current pos
    if pos != get_field_index("G2J") and pos not in community_chest_indexes and pos not in chances_indexes:
        return pos
    
    #go to jail
    if pos == get_field_index("G2J"):
        return get_field_index("JAIL")
    #community chest
    elif pos in community_chest_indexes:
        # "draw a card"
        roll = random.randrange(1,17)

        #for roll 1-2 go to appropiate position
        if roll == 1:
            # Advance to GO
            return get_field_index("GO")
            
        elif roll == 2: 
            # Go to JAIL
            return get_field_index("JAIL")
        #card that didn't affect position
        else:
            return pos 
            
    elif pos in chances_indexes:
        #draw a card
        roll = random.randrange(1,17)
        #for rolls 1-10 go to appropiate position
        if roll == 1:
            # Advance to GO
            return get_field_index("GO")
            
        elif roll == 2: 
            # Go to JAIL
            return get_field_index("JAIL")
            
        elif roll == 3:
            #Go to C1
            return get_field_index("C1")
            
        elif roll == 4:
            #Go to E3
            return get_field_index("E3")
            
        elif roll == 5:
            #Go to H2
            return get_field_index("H2")
            
        elif roll == 6:
            #Go to R1
            return get_field_index("R1")
            
        elif roll == 7 or roll == 8:
            #Go to next R (railway company)
            return get_next_railway_index(pos)
            
        elif roll == 9:
            #Go to next U (utility company)
            return get_next_utility_index(pos)
            
        elif roll == 10:
            # Go back 3 squares. modulu to "wrap around" 
            return get_position_after_special((pos + len(field_names)-3)%len(field_names))
        else:
            # card didn't affect position
            return pos
        
for i in range(iterations):
    visits[pos] += 1
    #roll two dice
    dice_one = random.randrange(1,num_sides+1)
    dice_two = random.randrange(1,num_sides+1) 

    #check for doubles
    if dice_one == dice_two:
        doubles_counter += 1
    else:
        doubles_counter = 0 
    
    # three consecutive doubles -> go to jail 
    if doubles_counter == 3:
        doubles_counter = 0
        pos = get_field_index("JAIL")
        #early return
        continue
        
    
    dice_sum = dice_one + dice_two
    #advance to new position
    pos = (pos+dice_sum)%len(field_names)
    #take into account special squares G2J, CC, CH
    pos = get_position_after_special(pos)
            

#build an array with (index, chance, field_name)
distribution_pair = [(i, visits[i]/iterations, field_names[i]) for i in range(40)]

#sort by chance (descending)
distribution_pair.sort(key=lambda pair:pair[1],reverse=True)

#print distribution for debugging
print(distribution_pair)
#first 3 indexes for modal string
solution_indexes=  [pair[0] for pair in distribution_pair[:3:]]
#pad to 2 digits
padded_solution_indexes = ["%2d" % index for index in solution_indexes]
#concat padded_solution_indexes
print("".join(padded_solution_indexes))