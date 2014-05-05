#-*- encoding:utf-8 -*-
#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.

from time import time

t = time()

def nextnum(number):
	divisors = []
	for i in range(2, int(number**0.5)):
		if number % i == 0:
			divisors.append(i)
			divisors.append(number/i)
	return sum(divisors)+1

maxchain = set()
nonmax = set([1])

for i in range(2, 10**5):
	chain = set()
	chain.add(i)
	n = i
	while True:
		n = nextnum(n)
		if n in nonmax or n < i or n == 1 or n > 10**6:
			nonmax.update(chain)
			chain = set()
			break
		if n not in chain: chain.add(n)
		else: break
	if n == i and len(chain) > len(maxchain): 
		nonmax.update(maxchain)
		maxchain = chain

print min(maxchain), time()-t