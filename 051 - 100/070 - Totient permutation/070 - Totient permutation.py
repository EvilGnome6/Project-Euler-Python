# -*- encoding: utf-8 -*-
#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

#Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

#in order to minimize n/φ(n), we are looking for a product of two prime factors close to 10^7
#the √ of 10^7 = 3162.28 so we'll generate primes between 2000 and 4000 since one of the primes will be below that number and the other will be above it

limit = 4000
primes = []
sieve = [True]*limit

for i in range(2, limit):
	if sieve[i] == True:
		if i > 2000: primes.append(i)
		for j in range(i*i, limit, i):
			sieve[j] = False

primeset = set(primes)

#For a semiprime n = pq the value of Euler's totient function (the number of positive integers less than or equal to n that are relatively prime to n) is particularly simple when p and q are distinct:
#φ(n) = (p − 1) (q − 1)

def gettotient(p, q):
	return (p - 1) * (q - 1)
	
minratio = 2.0

for i in range(0, len(primes)):
	factor1 = primes[i]
	for j in range(i, len(primes)):
		factor2 = primes[j]
		number = factor1 * factor2
		if number > 10000000: break
		totient = gettotient(factor1, factor2)
		if sorted(str(number)) == sorted(str(totient)):
			ratio = float(number) / totient
			if ratio < minratio:
				minratio = ratio
				print number, factor1, factor2, totient, ratio

