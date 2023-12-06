import numpy as np 

limit = 100
#get a numpy arrays with all numbers from [1,..,limit]
arr = np.arange(1,limit+1)

#get the sum of squared terms (1**2+...+limit**2)
sum_squared = arr.sum()**2
#get the square the sum of terms (1+...+limit)**2
squared_sum = (arr**2).sum()
#print difference
print(sum_squared-squared_sum)