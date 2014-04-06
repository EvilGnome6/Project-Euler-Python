# -*- encoding: utf-8 -*-
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

#1! + 4! + 5! = 1 + 24 + 120 = 145

#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872

#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)

#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

limit = 6

facts = dict({0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880})

def getfactsum(number):
	factsum = 0
	while number > 0:
		factsum += facts[number % 10]
		number /= 10
	return factsum

count = 0
cache = dict()
		
for i in range(3, limit):
	number = i
	chain = [number]
	length = 0
	
	while True:
		if number in cache:
			length = cache[number]
			print number, length
			break
		else: 
			number = getfactsum(number)
			if number in chain: break
			else: chain.append(number)
	
	if len(chain) + length == 60: 
		count += 1
#		print chain
	
	for num in range(0,len(chain)):
		cache.update({chain[num]:len(chain)-num+length})
		if num == number: break
	
	print chain, cache

#for num in cache:
#	print num, cache[num]
print count, len(cache)
