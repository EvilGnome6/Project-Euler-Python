#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

limit = 28123

# generate list of abundant numbers

abnums = []
for i in range(12, limit, 1):
	divisors = [1]
	for j in range(2, (i/2)+1, 1):
		if i % j == 0: divisors.append(j)
	if sum(divisors) > i: abnums.append(i)

# function to test if a number is the sum of two abundant numbers

abnumsset = set(abnums)

def issum(num):
	for i in range(0, len(abnums)/2):
		diff = num - abnums[i]
		if diff < (num/2): return False
		if diff in abnumsset: return True
	return False

# run through numbers in range and total the sum of all the numbers which are not the sum of two abundant numbers

sum = 0
for i in range(limit):
	if issum(i) == False: sum += i

print(sum)
