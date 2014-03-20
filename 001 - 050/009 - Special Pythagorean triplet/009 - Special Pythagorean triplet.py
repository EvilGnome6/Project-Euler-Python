#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

sum = 0
miniter = 200
maxiter = 426

for a in range(miniter, maxiter):
	for b in range(miniter, maxiter):
		for c in range(miniter, maxiter):
			if a**2 + b**2 == c**2:
				if a + b + c == 1000:
					print("a:" + str(a) + " b:" + str(b) + " c:" + str(c) + " is a triplet with a sum of " + str(a + b + c))
					print("the product of abc is " + str(a*b*c))
			c = c + 1
		c = miniter
		b = b + 1
	b = miniter
	a = a + 1

	
	