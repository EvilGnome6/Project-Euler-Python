#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

import itertools

limit = 10000
primes = []
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True: primes.append(i)
	for j in range(i**2, limit, i):
		sieve[j] = False

primeset = set(primes)

matchlist = []
for i in range(168, 1229):

	testlist = []
	perms = [int(''.join(x)) for x in itertools.permutations(str(primes[i]))]

	for p in perms:
		if p in primeset:
			if len(str(p)) == 4 and p not in testlist: testlist.append(p)
			testlist.sort()

	if len(testlist) >= 3:
		difflist=[]

		for j in range(0, len(testlist)):
			for k in range(j+1, len(testlist)):
				difflist.append(testlist[k]-testlist[j])

		for diff in difflist:
			if difflist.count(3330) == 2:
				if testlist not in matchlist: matchlist.append(testlist)
				break

results = []

for match in matchlist:

	result = []

	for i in range(0, len(match)):
		for j in range(i+1, len(match)):
			if match[j] - match[i] == 3330:
				if match[i] not in result: result.append(match[i])
				if match[j] not in result: result.append(match[j])
	results.append(result)
	
print results

for result in results:
	output = ""
	for num in result:
		output += str(num)
	print output
