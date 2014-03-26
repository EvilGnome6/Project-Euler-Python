#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def sumdigits(number):
	dsum = 0
	numstring = str(number)
	for digit in numstring:
		dsum += int(digit)
	return dsum

maxsum = 0

for a in range(1, 100):
	for b in range(1, 100):
		number = a**b
		digitsum = sumdigits(number)
		if digitsum > maxsum: 
			maxsum = digitsum
			base = a
			expo = b
			
print maxsum, base, expo