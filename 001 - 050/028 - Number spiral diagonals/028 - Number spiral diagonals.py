#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


size = 5

grid = [0] * (size+1)

for i in range(size+1):
	row = [0] * (size+1)
	grid[i]=row

for a in grid: print(a)

r = (size-1)/2
c = (size-1)/2

for num in range(1, size**2+1):
	grid[r][c]=num
	if num == 1:
		c += 1
	elif grid[r+1][c] == 0 and grid[r][c-1] != 0:
		if r < size: r += 1
	elif grid[r][c-1] == 0 and grid[r-1][c] != 0:
		if c < size: c -= 1
	elif grid[r-1][c] == 0 and grid[r][c+1] != 0:
		if r < size: r -= 1
	elif grid[r][c+1] == 0 and grid[r+1][c] != 0:
		if c < size: c += 1

ldiag = 0
rdiag = 0

for i in range(0, size, 1):
	ldiag += grid[i][i]
	rdiag += grid[i][size-i-1]

print(ldiag + rdiag - 1)