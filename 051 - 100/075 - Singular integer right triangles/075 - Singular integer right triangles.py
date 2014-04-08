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

#http://en.wikipedia.org/wiki/Farey_sequence
#a/b and c/d are the two given entries, and p/q is the unknown next entry
#k = (n + b)/d, p = kc − a and q = kd − b

def farey(n):
	a,b = 1,n
	c,d = 1,n-1
	primes = [[a,b],[c,d]]
	while c <= n:
		k = (n+b)/d
		a,b,c,d = c,d,k*c-a,k*d-b
		primes.append([c,d])
	return primes
	
coprimes = farey(10)

for pair in coprimes:
	m, n = pair[1], pair[0]
	if m < n: m, n = n, m
	if (m-n) % 2 != 0:
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		print m, n, a, b, c, a+b+c
	