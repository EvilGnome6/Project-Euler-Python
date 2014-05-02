#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).


#Euclid's formulae for a Pythagorean triple:
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2

from time import time
from fractions import gcd

t = time()

mnums = [1, 2, 3, 4, 7, 11, 15, 26, 41, 56, 97, 153, 209, 362, 571, 780, 1351, 2131, 2911, 5042, 7953, 10864, 18817, 29681, 40545]
nnums = [1, 4, 15, 56, 209, 780, 2911, 10864, 40545, 151316]

limit = 10**9
psum = 0

for n in nnums:
	for m in mnums:
		if m > n and ((m+n) % 2) == 1 and gcd(m,n) == 1:
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			if b*2 == c-1 or b*2 == c+1: 
				p = 2*(b+c)
				if p < limit: 
					psum += p
			if a*2 == c-1 or a*2 == c+1: 
				p = 2*(a+c)
				if p < limit: 
					psum += p

print 'per total:', psum
print 'calc time:', time()-t, 'ms'

