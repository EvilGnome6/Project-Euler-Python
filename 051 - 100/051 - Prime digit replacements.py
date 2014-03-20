#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

limit = 100000
primes = []
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

primeset = set(primes)

#print primes
#print primes.index(10007)

primelength = 0

for i in range(1229, len(primes)):
	primelist = []
	for j in range(0, 10):
#		print str(primes[i])[0:]
#		newprime = int(str(primes[i])[0] + str(primes[i])[1] + str(j) + str(j) + str(primes[i])[-1:])
#		newprime = int(str(primes[i])[0] + str(j) + str(primes[i])[2] + str(j) + str(primes[i])[-1:])
#		newprime = int(str(primes[i])[0] + str(j) + str(j) + str(primes[i])[3] + str(primes[i])[-1:])
#		newprime = int(str(j) + str(primes[i])[1] + str(j) + str(primes[i])[3] + str(primes[i])[-1:])
		newprime = int(str(j) + str(j) + str(primes[i])[2] + str(primes[i])[3] + str(primes[i])[-1:])
#		print newprime
		if newprime in primeset:
			primelist.append(newprime)
			if len(primelist) > primelength:
				primelength = len(primelist)
				print primelist, len(primelist)