#n! means n x (n - 1) x ... x 3 x 2 x 1

#For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

number = 100

fact = 1
for n in range(1, number+1, 1):
	fact = fact * n

digits = str(fact)
sum = 0
for n in range(0, len(digits), 1):
	sum = sum + int(digits[n])

print(sum)