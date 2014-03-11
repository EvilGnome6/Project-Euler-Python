#	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#	Find the sum of all the primes below two million.

n = 2000000

sieve = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i*i, n + 1, i):
			sieve[j] = False

print(sum(primes))
