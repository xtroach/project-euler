import random
field_str = "GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3, JAIL, C1, U1, C2, C3, R2, D1, CC2, D2, D3, FP, E1, CH2, E2, E3, R3, F1, F2, U2, F3, G2J, G1, G2, CC3, G3, R4, CH3, H1, T2, H2"
field_names = field_str.replace(" ","").split(",")


pasch_counter = 0 
num_sides = 6
iterations = 10**2
pos = 0
def get_field_index(field_name):
    return field_names.index(field_name)

chances_indexes = [get_field_index("CH1"), get_field_index("CH2"), get_field_index("CH3")]
community_chest_indexes = [get_field_index("CC1"),get_field_index("CC2"),get_field_index("CC3")]

visits = [0 for _ in range(0,40)]

for i in range(iterations):
    visits[pos] += 1 
    dice_one = random.randrange(1,num_sides+1)
    dice_two = random.randrange(1,num_sides+1) 

    if dice_one == dice_two:
        pasch_counter += 1
    
    if pasch_counter == 3:
        pasch_counter = 0
        pos = 0
        continue
    
    dice_sum = dice_one + dice_two

    pos = (pos+dice_sum)%len(field_names)

    if pos in chances_indexes:
        pass
    elif pos in community_chest_indexes:
        roll = random.randrange(1,17)
        if roll == 1:
            # Advance to GO
            pos = get_field_index("GO")
            continue
        elif roll == 2: 
            # Go to JAIL
            pos = get_field_index("JAIL")
            continue
        elif roll == 3:
            #Go to C1
            pos = get_field_index("C1")
            continue
        elif roll == 4:
            #Go to E3
            pos = get_field_index("E3")
        elif roll == 5:    Advance to GO
    Go to JAIL
    Go to C1
    Go to E3
    Go to H2
    Go to R1
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.

            #Go to H2
            pos = get_field_index("H2")
        elif roll == 6:
            #Go to R1
            pos = get_field_index("R1")
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.
