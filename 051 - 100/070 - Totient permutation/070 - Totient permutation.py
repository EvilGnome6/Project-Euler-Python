# -*- encoding: utf-8 -*-
#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

#Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

limit = 10000
primes = []
sieve = [True]*limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i*i, limit, i):
			sieve[j] = False

primeset = set(primes)
#print primes

def getfactors(number):
	factors = []
	if number in primeset:
		factors.append(number)
		return factors
	for p in primes:
		if number % p == 0:
			factors.append(p)
			while number % p == 0:
				number /= p	
			if number in primeset:
				factors.append(number)
				return factors
	return factors

for i in range(2, 10000):
	print i, getfactors(i)
