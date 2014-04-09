#It is possible to write five as a sum in exactly six different ways:

#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1

#How many different ways can one hundred be written as a sum of at least two positive integers?

total = 100
digits = range(1, 100)
ways = [1] + [0]*total

for d in digits:
	for i in range(d, total+1):
		ways[i] += ways[i-d]

print ways[total]