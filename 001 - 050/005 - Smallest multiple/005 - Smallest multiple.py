#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

numbers = []
factors = []
allfactors = []
numfactors =[]
multiple = 1

#populate numbers array with integers

i=1
while i in range(1, 20):
	numbers.append(i)
	i = i + 1

# function returns factors of an integer

def getfactors(number):
	factor = 2
	
	while factor <= number:
		if number % factor == 0:
			while number % factor == 0:
				factors.append(factor)
				number = number / factor
		factor = factor + 1
	return(factors)

# collect the factors of all the numbers

i = 1
while i in range(1, len(numbers)):
	numfactors = getfactors(numbers[i])

# if the count of a factor from any of the numbers is greater than the count in the allfactors, add it to allfactors

	j = 0
	while j in range(0,len(numfactors)):
		count = numfactors.count(numfactors[j])
#		print(str(count) + " " + str(numfactors[j]))
		if count > allfactors.count(numfactors[j]):
			allfactors.append(numfactors[j])
#			print(allfactors)
		j = j + 1
	
	del numfactors[:]
	i = i + 1

# multiply all the factors in allfactors to calculate lowest common multiple of all numbers

i = 0
while i in range(0, len(allfactors)):
	multiple = multiple * allfactors[i]
	i = i + 1

print("The lowest common multiple is " + str(multiple))