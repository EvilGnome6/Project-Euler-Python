#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

#note: The limit of 7654321 was determined as follows
#
#If the sum of digits is divisible by 3, then the number is a multiple of 3 and definitely not a prime.
#1+2+3+4+5 = 15, therefore 12345 is divisible by 3
#1+2+..+7+8 = 36 and 1+2+..+8+9=45 are both divisble by three so there are no pandigital primes with all those numbers
#1+2+3+4+5+6+7 = 28 and is the largest set of numbers that is not a multiple of three

limit = 7654321

def isprime(number):
	for i in range(2, int(number**0.5)+1):
		if number % i == 0: return False
	return True

def ispandigital(number):
	if str(number).count('0') or str(number).count('9') or str(number).count('8')> 0:
		return False
	for i in range(1, 8):
		if str(number).count(str(i)) > 1:
			return False
	return True
	
while True:
	if ispandigital(limit) == True:
		if isprime(limit) == True:
			print limit
			break
	limit -= 1
