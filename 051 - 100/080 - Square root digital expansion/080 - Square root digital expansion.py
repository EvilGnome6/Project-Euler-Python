#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


def sqrt(n):
	rt = int(n ** 0.5)
	if rt ** 2 == n: return 0
	n -= rt ** 2
	for i in range(99):
		n = n * 100
		d = rt * 20
		d1 = n / d
		d += d1
		if d * d1 > n:
			d -= 1
			d1 -= 1
		n -= d * d1
		rt = rt * 10 + d1
	return rt

def digitsum(num):
	number = str(sqrt(num))
	total = 0
	for n in number:
		total += int(n)
	return total

total = 0
for i in range(1, 101):
	total += digitsum(i)
print total