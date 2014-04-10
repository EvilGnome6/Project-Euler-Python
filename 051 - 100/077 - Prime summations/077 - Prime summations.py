#It is possible to write ten as the sum of primes in exactly five different ways:

#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2

#What is the first value which can be written as the sum of primes in over five thousand different ways?

limit = 10
primes = []
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

print primes

def getways(number):
	ways = [1] + [0]*limit

	return ways[limit]

print getways(10)
	
