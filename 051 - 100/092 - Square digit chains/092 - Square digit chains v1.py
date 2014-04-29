# -*- encoding: utf-8 -*-
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

limit = 10**6

set1 = set([1])
set89 = set([89])
loop89 = 0

def sqsum(num):
	total = 0
	while num > 0:
		total += (num % 10)**2
		num /= 10
	return total

for num in range(1, limit+1):
	
	strnum = str(num)
	num = int(''.join(sorted(strnum)))
	
	if num in set89:
		loop89 += 1
		continue
	if num in set1:
		continue
	
	nextnum = sqsum(num)
	
	tset = set([num])
	while True:
		if nextnum in set89:
			loop89 += 1
			set89.update(tset)
			break
		if nextnum in set1:
			set1.update(tset)
			break
		nextnum = sqsum(nextnum)
		tset.add(nextnum)

print loop89
