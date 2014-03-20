# -*- encoding:utf-8 -*-
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

limit = 1001
integrals = []

def integral(perimeter):
	count = 0
	for b in range(1, perimeter/2):
		for a in range(1, perimeter/2):
			if b < a: break
			c = perimeter - (a + b)
			if a**2 + b**2 == c**2:
				count += 1
	return count
	
for i in range(2, limit, 2):
	if integral(i) > 4:
		integrals.append([i, integral(i)])
		print integrals
		
