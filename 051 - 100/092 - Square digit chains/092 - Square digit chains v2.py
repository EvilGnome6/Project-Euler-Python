# -*- encoding: utf-8 -*-
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

from math import factorial
from time import time

t = time()

def sqsum(num):
	total = 0
	while num > 0:
		total += (num % 10)**2
		num /= 10
	return total
	
def getchain(num):
	while True:
		if num == 89: return 89
		if num == 1: return 1
		num = sqsum(num)
		
def perms(strnum):
	nume = factorial(len(strnum))
	deno = 1
	for i in range(0,10):
		deno *= factorial(strnum.count(str(i)))
	return nume/deno

chain1 = set()
for num in range(1, 568):
	if getchain(num) == 1: chain1.add(num)

count = 0

for a in range(10):
	for b in range(a, 10):
		for c in range(b, 10):
			for d in range(c, 10):
				for e in range(d, 10):
					for f in range(e, 10):
						for g in range(max(1,f), 10):
							num = map(str,[a,b,c,d,e,f,g])
							num = ''.join(num)
							if sqsum(int(num)) in chain1:
								#print num, perms(num)
								count += perms(num)

print (10**7 -1) - count, time() - t

#print chain1