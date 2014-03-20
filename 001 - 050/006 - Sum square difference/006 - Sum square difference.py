#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sumsquare = 0
squaresum = 0
lastnum = 100
difference = 0

# calculate the sum of the squares

for i in range(1, lastnum + 1):
	sumsquare = sumsquare + (i * i)
	i = i + 1

# calculate the square of the sum

for i in range(1, lastnum + 1):
	squaresum = squaresum + i
	i = i + 1
squaresum = squaresum * squaresum

# calculate and print the difference

difference = squaresum - sumsquare
print("The difference is " + str(difference))

