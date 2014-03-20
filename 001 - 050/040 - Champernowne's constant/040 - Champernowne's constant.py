#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

limit = 1000000
constant = '.'

i = 1
while len(constant) < limit + 1:
	constant += str(i)
	i += 1

product = 1

i = 1
while i < 1000000:
	i *= 10
	product *= int(constant[i])

print product