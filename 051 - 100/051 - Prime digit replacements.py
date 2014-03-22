#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#Use a sieve of Eratosthenes to generate primes.

limit = 1000000
primes = []
sieve = [True] * limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

primeset = set(primes)

#This function takes a number and returns the maximum repetitions of a digit and which digit is most repeated.

def maxreps(number):
	maxreps = 0
	for i in range(0, 10):
		reps = str(number).count(str(i))
		if reps > maxreps: 
			maxreps = reps
			digit = i
	return maxreps, digit

#This function takes a number and a digit and return a mask based on any digits that match the given digit.

def getmask(number, digit):
	numbstring = str(number)
	mask = ''
	for char in numbstring:
		if char == str(digit): mask += '1'
		else: mask += '0'
	return mask
	
#Loop through prime numbers, starting at index 9592, which is the first prime with six digits.
for i in range(9592, len(primes)):
	prime = primes[i]
	primetest = maxreps(prime)
	#Look for primes that repeat a digit more than 2 times. If so, get the mask for the repeated digit.
	if primetest[0] > 2:
		mask = getmask(prime, primetest[1])
		primelist = []
		primestring = str(prime)
		#Use the mask to replace the repeated digit with numbers 0-9. If the modified number is prime, add it to a list.
		for i in range(0, 10):
			testprime = ''
			for char in primestring:
				if char != str(primetest[1]): testprime += char
				else: testprime += str(i)
			#Need to make sure that the prime is over 100000. The mask could have replace one or more leading digits with a 0.
			if int(testprime) > 100000:
				if int(testprime) in primeset:
					primelist.append(int(testprime))
		#Once we've found a list with 8 primes, we're done. Print the list and break out of the loop.
		if len(primelist) == 8:
			print primelist, len(primelist)
			break
