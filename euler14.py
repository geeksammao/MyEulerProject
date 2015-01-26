def calculate(n):
	if n % 2 != 0:
		n = n*3 + 1
	else:
		n = n/2
	return n	

dic = {}
for x in xrange(17,1000001):
	print x
	i = 0
	while x != 16:
		x = calculate(x)
		i += 1
	dic[x] = i
	
dic_new = sorted(dic.iteritems(), key = lambda d:d[1], reverse = True)

print dic_new[0]					