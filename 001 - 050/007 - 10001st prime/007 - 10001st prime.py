#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

primes = [2, 3]
position = 10001

# function to test if number is prime by trying to divide by all known primes before it

def testprime(num):
	i = 1
	while i in range(len(primes)):
		if primes[i] > int(num**0.5):
			return(True)
		if num % primes[i] == 0:
			return(False)
		i = i + 1
	return(True)

# add 2 to the last prime number and test if it is prime. If so, add it to the primes

nextnum = primes[len(primes)-1] + 2
while len(primes) < position:
	if testprime(nextnum) == True:
		primes.append(nextnum)
		print("position: " + str(len(primes)) + " prime: " + str(nextnum))
	nextnum = nextnum + 2
