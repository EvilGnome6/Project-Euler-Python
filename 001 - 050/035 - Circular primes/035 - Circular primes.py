#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

limit = 1000000
primes = set()

sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.add(i)
		for j in range(i*i, limit, i):
			sieve[j] = False

circularsum = 0

for i in range(2, limit):
	if i in primes:
		numberstr = str(i)
		numlength = len(numberstr)
		circular = True
		
		if numlength == 1:
			circular = True
			
		if numlength > 1:
			for j in range(1, numlength):
				numberstr = numberstr[1:numlength+1] + numberstr[0] 
				if int(numberstr) not in primes:
					circular = False
					
		if circular == True: circularsum += 1
		
print circularsum