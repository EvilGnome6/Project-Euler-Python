# -*- encoding: utf-8 -*-
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

start = 100000
limit = 200000
cons = 4

primes = []
sieve = [True] * int(limit)

for i in range(2, int(limit)):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

primeset = set(primes)

def getfactors(number):
	factors = []
	
	if number in primeset: 
		factors.append(number)
		return factors
		
	for p in primes:
		if number % p == 0:
			factors.append(p)
			while number % p == 0:
				number = number / p
			if number == 1: return factors

factors = []
for i in range(start, limit):
	factors.append(getfactors(i))
	if len(factors) == cons:
		distinct = True
		for factor in factors:
			if len(factor) != cons:	
				distinct = False
				break
		if distinct == True: 
			print i-cons+1, factors
			break
		factors.pop(0)
				