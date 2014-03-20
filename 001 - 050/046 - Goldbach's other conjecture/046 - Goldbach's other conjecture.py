# -*- encoding: utf-8 -*-
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

limit = 5800

primes = set()
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.add(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

comps = []

for i in range(3, limit, 2):
	if sieve[i] == False: comps.append(i)

squares = set()

for i in range(1, limit):
	squares.add(2*(i**2))
	
for comp in comps:
	conj = False
	for prime in primes:
		if comp - prime in squares:
			conj = True
			break
	if conj == False: print comp
