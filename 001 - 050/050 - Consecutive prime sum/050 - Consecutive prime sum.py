#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13

#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

limit = 1000000

primes = []
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

primeset = set(primes)

#print primeset

maxlength = 0

for i in range(0, 4):
	primesum = []
	primesum.append(primes[i])
	for j in range(i+1, len(primes)/5):
		primesum.append(primes[j])
		if len(primesum) > maxlength:
			if sum(primesum) in primeset:
				maxlength = len(primesum)
				print primesum, len(primesum), sum(primesum)