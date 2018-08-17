


def gen(listt, x):
	templist = listt
	if(len(listt) >= x):
		return listt 
		
	aclimit = len(listt) - 1
	limit = len(listt)*2
	print(aclimit)
	print(limit)
	list0 = [[0 for j in range(limit)] for i in range(limit)]
	a = 0
	b = 0
	count = 0
	for i in range(limit):
		for j in range(limit):
			if i >= limit / 2 and j >= limit / 2:
				list0[i][j] = templist[a][b] * -1
			else:
				list0[i][j] = templist[a][b]
			b += 1
			if b > aclimit:
				b = 0
			
		a += 1
		if a > aclimit:
			a = 0
			b = 0
		count += 1
	return gen(list0, x)
x = [[1]]
perlist = gen(x, 1)
for z in range(len(perlist)):
	print(perlist[z])
