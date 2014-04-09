# -*- encoding: utf-8 -*-
#It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)

#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

#120 cm: (30,40,50), (20,48,52), (24,45,51)

#Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

#Euclid's formulae for a Pythagorean triple:
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# p = a + b + c = 2m^2 + 2mn

from fractions import gcd

limit = 1500000

perimeters = [0] * (limit+1)

for m in range(1, 900):
	for n in range(1, 900):
		if m > n and ((m+n) % 2) == 1 and gcd(m,n) == 1:
			p = 2 * m * ( m + n )
			if p == 120: print m, n, p
			if p > limit: break
			for i in range(p, limit, p):
				perimeters[i] += 1
			
print perimeters.count(1)

#for i in range(121):
#	if perimeters[i] != 0: print i, perimeters[i]