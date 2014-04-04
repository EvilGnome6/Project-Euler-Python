# -*- encoding: utf-8 -*-
#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that there are 21 elements in this set.

#How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

limit = 1000000

fractions = range(0, limit+1)
fractions[1] = 0

for i in range(2, limit+1):
	if fractions[i] == i:
		for j in range(i, limit+1, i):
			fractions[j] = fractions[j] / i * (i-1)

print sum(fractions)