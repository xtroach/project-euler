
#function to calculate sum of alpha_numeric_values of a string
def alpha_numeric_sum(str):
    # ord('A') == 65  
    return sum([ord(char)-64 for char in str])

#open name file
f = open('problem0022_names.txt', 'r')
#read names into array, names are split by ","
names = f.read().split(",")
#close file
f.close()
#strip "" at start and end
names = [name.strip("\"") for name in names]
#sort alphabetically
names.sort()
#calcluate scores
names = [(name, alpha_numeric_sum(name)) for name in names]


sum = 0 
#sum up scores
for (i,(name,score)) in enumerate(names):
    index = i+1
    sum += index*score

print(sum)