'''
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''


limit = 50 * 10**6
#print limit

psquare = [4]
pcube = [8]
pfour = [16]
sieve = [True] * int(limit**0.5)

for i in range(3, int(limit**0.5), 2):
	if sieve[i] == True:
		psquare.append(i**2)
		pcube.append(i**3)
		pfour.append(i**4)
		for j in range(i**2, int(limit**0.5), i):
			sieve[j] = False

count = set()
for p4 in pfour:
	for p3 in pcube:
		if p3 + p4 > limit: break
		for p2 in psquare:
			sum = p2 + p3 + p4
			if sum > limit: break
			count.add(sum)

print len(count)
