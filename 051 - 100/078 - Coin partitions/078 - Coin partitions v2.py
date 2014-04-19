#-*- encoding: utf-8 -*-
#gk = k(3k-1)/2 for k = 1, −1, 2, −2, 3, ...

limit = 10
pents = []
for k in range(1, limit):
	pents.append(k*(3*k-1)/2)
	pents.append(-k*(3*-k-1)/2)

print pents

#The first few values of the partition function are (starting with p(0)=1):
#1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, …
#This theorem can be used to derive a recurrence for the partition function:
#p(k) = p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15) − p(k − 22) − ...
#where p(0) is taken to equal 1, and p(k) is taken to be zero for negative k.

sign = [1,1,-1,-1]
parts = [1]

for k in range(1, 2):
	part = 0

	for i in range(0, 2):
		s = sign[i%4]
		p = parts[k-pents[i]]
		print k, i, pents[i], s, p
		if p < 1 : break
		part += s*p

	parts.append(part)





	k = 1
	part = parts[k-pents[0]]
	parts.append(part)

	k = 2
	part = parts[k-pents[0]] + parts[k-pents[1]]
	parts.append(part)

	k = 3
	part = parts[k-pents[0]] + parts[k-pents[1]]# - parts[k-pents[2]]
	parts.append(part)

	k = 4
	part = parts[k-pents[0]] + parts[k-pents[1]]# - parts[k-pents[2]] - parts[k-pents[3]]
	parts.append(part)

	k = 5
	part = parts[k-pents[0]] + parts[k-pents[1]] - parts[k-pents[2]]# - parts[k-pents[3]] + parts[k-pents[4]]
	parts.append(part)
		
	print parts
