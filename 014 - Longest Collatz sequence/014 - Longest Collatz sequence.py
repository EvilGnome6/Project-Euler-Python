#The following iterative sequence is defined for the set of positive integers:

#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

#a.index(max(a))
#[0, 1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 10]

maxnum = 1000000

collatz = [0] * (maxnum + 1)

def getterms(num):
	count = 1
	while num > 1:
		if num < len(collatz):
			if collatz[num] > 0:
				count = count + collatz[num] - 1
				break
		if num % 2 == 0:
			num = num / 2
			count = count + 1
		else:
			num = num * 3 + 1
			count = count + 1
	return(count)
	
for i in range(1, maxnum+1):
	collatz[i]=getterms(i)

print(collatz.index(max(collatz)))
