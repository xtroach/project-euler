#iterate until 500 (slooppy aproximation)
a = 1 
for a in range(1,500):
	#still sloppy approximation
	for b in range(a+1,500):
		#since a+b+c=100
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print(a*b*c)

#TODO: bounds are sloppy, early breaking missing, probably can be heavily optimized