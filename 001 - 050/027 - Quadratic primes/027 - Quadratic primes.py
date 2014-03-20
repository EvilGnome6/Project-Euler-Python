#Euler discovered the remarkable quadratic formula:

#n^2 + n + 41

#It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

#The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

#Considering quadratics of the form:

#    n^2 + an + b, where |a| < 1000 and |b| < 1000

#    where |n| is the modulus/absolute value of n
#    e.g. |11| = 11 and |-4| = 4

#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.


#generate list of prime numbers

n = 4000
sieve = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
	if sieve[i] == True:
		primes.append(i)
	for j in range((i*i), (n + 1), i):
		sieve[j] = False

#function will return the longest streak for a pair of coefficients

def getstreak(a, b):
	streak = []
	for n in range(0, 100):
		result = n**2 + n*a + b
		if result in primes:
			streak.append(result)
		else:
			break
	return streak

#find the coefficiencts that generate the longest streak

limit = 1000
longest = 0
for a in range(-limit, limit):
	for b in range(-limit, limit):
		streak = getstreak(a, b)
		if len(streak) > longest:
			longest = len(streak)
			coefficients = "a = " + str(a) + ", b = " + str(b) + ", product = " + str(a*b)

print(coefficients)