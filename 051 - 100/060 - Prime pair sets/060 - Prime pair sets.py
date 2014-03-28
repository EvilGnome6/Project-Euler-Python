#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

limit = 10000
primes = []
sieve = [True]*limit

for i in range(2, limit):
	if sieve[i] == True:
		primes.append(i)
		for j in range(i**2, limit, i):
			sieve[j] = False

def isprime(number):
	if number % 2 == 0: return False
	for i in range(3, (int(number**0.5))+1, 2):
		if number % i == 0: return False
	return True

def test2primes(p1, p2):
	if isprime(int(str(p1)+str(p2))) == False: return False
	if isprime(int(str(p2)+str(p1))) == False: return False
	return True

def test3primes(p1, p2, p3):
	if isprime(int(str(p1)+str(p3))) == False: return False
	if isprime(int(str(p2)+str(p3))) == False: return False
	if isprime(int(str(p3)+str(p1))) == False: return False
	if isprime(int(str(p3)+str(p2))) == False: return False
	return True

def test4primes(p1, p2, p3, p4):
	if isprime(int(str(p1)+str(p4))) == False: return False
	if isprime(int(str(p2)+str(p4))) == False: return False
	if isprime(int(str(p3)+str(p4))) == False: return False
	if isprime(int(str(p4)+str(p1))) == False: return False
	if isprime(int(str(p4)+str(p2))) == False: return False
	if isprime(int(str(p4)+str(p3))) == False: return False
	return True

def test5primes(p1, p2, p3, p4, p5):
	if isprime(int(str(p1)+str(p5))) == False: return False
	if isprime(int(str(p2)+str(p5))) == False: return False
	if isprime(int(str(p3)+str(p5))) == False: return False
	if isprime(int(str(p4)+str(p5))) == False: return False
	if isprime(int(str(p5)+str(p1))) == False: return False
	if isprime(int(str(p5)+str(p2))) == False: return False
	if isprime(int(str(p5)+str(p3))) == False: return False
	if isprime(int(str(p5)+str(p4))) == False: return False
	return True
	
solved = False
for p1 in range(0, len(primes)):
	if solved == True: break
	for p2 in range(p1+1, len(primes)):
		if solved == True: break
		if test2primes(primes[p1], primes[p2]) == True:
			for p3 in range(p2+1, len(primes)):
				if solved == True: break
				if test3primes(primes[p1], primes[p2], primes[p3]) == True:
					for p4 in range(p3+1, len(primes)):
						if solved == True: break
						if test4primes(primes[p1], primes[p2], primes[p3], primes[p4]) == True:
							for p5 in range(p4+1,  len(primes)):
								if solved == True: break
								if test5primes(primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]) == True:
									total = primes[p1] + primes[p2] + primes[p3] + primes[p4] + primes[p5]
									print primes[p1], primes[p2], primes[p3], primes[p4], primes[p5], total
									solved = True
					