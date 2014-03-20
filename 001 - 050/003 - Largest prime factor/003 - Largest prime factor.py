#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


number = 600851475143
factor = 3
factors = []

while factor <= number:

	if number % factor == 0:
		factors.append(factor)
		number = number / factor

	factor = factor + 2

print ("the largest prime factor is " + str(factors[len(factors)-1]))