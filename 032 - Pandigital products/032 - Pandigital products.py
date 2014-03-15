# -*- coding: utf-8 -*-
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pandnumbers = []

for i in range(1, 100):
	for j in range(1, 2000):
		pandigital = False
		product = i * j
		prodstring = str(i) + str(j) + str(product)
		if len(prodstring) == 9:
			for number in numbers:
				if number in prodstring:
					pandigital = True
				else:
					pandigital = False
					break
			if pandigital == True:
				if product not in pandnumbers: pandnumbers.append(product)
				print(i, j, product)


print(pandnumbers, sum(pandnumbers))