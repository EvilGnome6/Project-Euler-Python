#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O

#Find the least value of n for which p(n) is divisible by one million.

def getways(n):
	ways = [1]+[0]*n
	piles = range(1,n+1)
	for p in piles:
		for i in range(p, (n+1)):
			ways[i] += ways[i-p]
		if ways[p] % 1000000 == 0: 
			return p
			break

print getways(100000)
	