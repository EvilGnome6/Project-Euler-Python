# -*- encoding: utf-8 -*-
'''
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

limit = 24000

minsum = [0] * 24001

def getfactors(number):
	factors = []
	for i in range(2, int(number**0.5)+1):
		f = []
		if number % i == 0:
			f.append(i)
			f.append(number/i)
			factors.append(f)
	nextf = []
	for f in factors:
		nf = nextfactors(f)
		for n in nf:
			if n not in factors: factors.append(n)
	return factors

def nextfactors(factors):
	nextf = []
	lastnum = factors[-1]
	for i in range(2, int(lastnum**0.5)+1):
		if lastnum % i == 0:
			f = list(factors)
			f[-1] = i
			f.append(lastnum/i)
			f.sort()
			nextf.append(f)
	return nextf

def minpsum(factors):
	for f in factors:
		fprod = 1
		for n in f: fprod *= n
		fsum = sum(f)
		k = fprod - fsum + len(f)
		if minsum[k] == 0:
			minsum[k] = fprod
		elif minsum[k] > fprod:
			minsum[k] = fprod

for i in range(4, limit):
	factors = getfactors(i)
	minpsum(factors)

minset = set()

for m in range(2,12001):
	minset.add(minsum[m])
	
print sum(minset)