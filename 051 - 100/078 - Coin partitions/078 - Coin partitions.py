#-*- encoding: utf-8 -*-
#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O

#Find the least value of n for which p(n) is divisible by one million.

#generate pentagonal numbers:
#gk = k(3k-1)/2 for k = 1, −1, 2, −2, 3, ...

limit = 100000
pents = []
for k in range(1, 200):
	pents.append(k*(3*k-1)/2)
	pents.append(-k*(3*-k-1)/2)

#Use pentagonal numbers with Euler's partition generating function.
#The first few values of the partition function are (starting with p(0)=1):
#1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, …
#This theorem can be used to derive a recurrence for the partition function:
#p(k) = p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15) − p(k − 22) − ...
#where p(0) is taken to equal 1, and p(k) is taken to be zero for negative k.

sign = [1,1,-1,-1]
parts = [1]

for n in range(1, limit):
	part = 0

	for i in range(0, limit):
		s = sign[i % 4]
		j = n - pents[i]
		if j < 0: break
		p = parts[j]
		part += s*p
	
	part %= 1000000
	parts.append(part)
	if part % 1000000 == 0: break

print "n:", n
