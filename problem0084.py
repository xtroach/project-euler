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
    
    dice_one = random.randrange(1,num_sides+1)
    dice_two = random.randrange(1,num_sides+1) 

    if dice_one == dice_two:
        pasch_counter += 1
    
print(visits)