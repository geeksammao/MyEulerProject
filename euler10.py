def is_prime(n):
	for x in xrange(2,int(n**(0.5))+1):
		if n%x == 0:
			return False


list = []
sum = 0

for x in xrange(2,2000000):
	if is_prime(x) != False:
	 	list.append(x)

for x in list:
	sum += x

print sum 

