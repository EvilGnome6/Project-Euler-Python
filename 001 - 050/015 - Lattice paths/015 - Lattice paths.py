#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20x20 grid?

grid = 20

def fact(num):
	fact = 1
	for i in range(1, num):
		fact = fact * num
		num = num - 1
		i = i + 1
	return(fact)

paths = fact(grid * 2) / (fact(grid) * fact(grid))

print(paths)