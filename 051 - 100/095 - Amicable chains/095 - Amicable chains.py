#-*- encoding:utf-8 -*-
#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.


def nextnum(number):
	divisors = []
	for i in range(2, int(number**0.5)):
		if number % i == 0:
			divisors.append(i)
			divisors.append(number/i)
	return sum(divisors)+1
	
#print nextnum(12496), nextnum(14288), nextnum(15472), nextnum(14536), nextnum(14264)
#print nextnum(12495), nextnum(12129), nextnum(5343), nextnum(2385), nextnum(1827), nextnum(1293), nextnum(435), nextnum(285), nextnum(195), nextnum(113)

chain = []
n = 1064
while True:
	chain.append(n)
	n = nextnum(n)
	if n in chain: break
print chain, len(chain)

maxchain = set()
pathto1 = set([1])
pathtomax = set([10**6])

for i in range(2, 10**5):
	chain = set()
	chain.add(i)
	n = nextnum(i)
	while True:
		if n in pathto1:
			pathto1.update(chain)
			chain = set()
			break
		if n > 10**6:
			pathtomax.update(chain)
			chain = set()
			break
		if n in pathtomax:
			pathtomax.update(chain)
			chain = set()
			break
		if n not in chain: chain.add(n)
		else: break
		n = nextnum(n)
	if len(chain) > len(maxchain): maxchain = chain

print len(pathto1), len(pathtomax)
print maxchain, min(maxchain), len(maxchain)