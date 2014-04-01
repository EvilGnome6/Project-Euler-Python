#-*- encoding: utf-8 -*-
#Consider quadratic Diophantine equations of the form:

#x^2 – Dy^2 = 1

#For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

#It can be assumed that there are no solutions in positive integers when D is square.

#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

#3^2 – 2×2^2 = 1
#2^2 – 3×1^2 = 1
#9^2 – 5×4^2 = 1
#5^2 – 6×2^2 = 1
#8^2 – 7×3^2 = 1

#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

def solvexy(d):
	a = int(d**0.5)
	if d**0.5 == a: return [0,0,0]
	expansions = [[0,0,1],[0,1,0],[a,0,0]]
	numea = 0 - a
	deno = 1
	i = 2
	
	while True:
		numea, deno = deno, numea
		numeb = deno * -1
		deno = d - deno**2
		deno = deno / numea
		numea = 1
		a = int((d**0.5 + numeb)/deno)
		numeb = numeb - (a * deno)
		numea = numeb
		expansions.append([a,0,0])
		expansions[i][1] = (expansions[i][0] * expansions[i-1][1]) + expansions[i-2][1]
		expansions[i][2] = (expansions[i][0] * expansions[i-1][2]) + expansions[i-2][2]
		x = expansions[i][1]
		y = expansions[i][2]
		
		if x**2 - d * (y**2) == 1: return [x,y,d]
		i += 1

xmax = [0,0,0]

for i in range(1000):
	xtest = solvexy(i)
	if xtest[0] > xmax[0]:
		xmax = xtest
		print xmax