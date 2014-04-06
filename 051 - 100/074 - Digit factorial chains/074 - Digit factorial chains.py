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

limit = 10000

import math
import itertools

def nextfactorial(number):
	nextnum = 0
	numstring = str(number)
	for num in numstring:
		nextnum += math.factorial(int(num))
	return nextnum

def getfactchain(number):
	chain = [number]
	while True:
		number = nextfactorial(number)
		if number in chain:
			chain.append(number)
			return chain
		chain.append(number)

count = 0
skipped = 0
factchains = dict()

for i in range(3, limit):
	sortnum = int(''.join(sorted(str(i))))
	print sortnum
	if sortnum in factchains:
		length = factchains[sortnum]
		factchains.update({i:length})
		if length == 60:
			count += 1
	
	if i not in factchains:
		chain = getfactchain(i)
		repnum = chain[-1]
		reppos = chain.index(repnum)
		length = len(chain)-1
#		print chain, repnum, reppos, length
		for j in range(0, len(chain)):
			sortnum = int(''.join(sorted(str(chain[j]))))
			if j < reppos:
				factchains.update({chain[j]:(length)-j})
				if length - j == 60: count += 1
				if "0" not in str(sortnum):
					factchains.update({sortnum:(length-j)})
					if length - j == 60: count += 1
			if j > reppos:
				factchains.update({chain[j]:length-reppos})
				if length - reppos == 60: count += 1
				if "0" not in str(sortnum):
					factchains.update({sortnum:length-reppos})
					if length-reppos == 60: count += 1

	else: skipped += 1

#for chain in factchains:
#	print chain, factchains[chain]

print count, skipped