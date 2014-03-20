#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.


import math
total = 0

for number in range(3, 50000):
	digits = []
	factsum = 0
	for i in range(0, len(str(number))):
		digits.append(int(str(number)[i]))
	for i in range(len(digits)):
		factsum += math.factorial(digits[i])
	if factsum == number:
		total += number
		print(number, total)
