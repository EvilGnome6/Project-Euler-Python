#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

limit = 739398
sieve = [True] * limit
primes = set()
truncprimes = []

for i in range(2, limit):
	if sieve[i] == True:
		primes.add(i)
		for j in range(i**2, limit, i):
			sieve[j]=False

for i in primes:
	truncatable = False
	if i in primes and i > 20: 
		truncatable = True
		for j in range(0, len(str(i))-1):
			if int(str(i)[0:j+1]) not in primes or int(str(i)[j+1::]) not in primes:
				truncatable = False
				break
	
	if truncatable == True:
		truncprimes.append(i)
		print truncprimes, sum(truncprimes)