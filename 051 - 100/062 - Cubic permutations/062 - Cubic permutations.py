#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

cubes = [0]*10000

for i in range(5000, 8400):
	cube = i**3
	digcount = []
	for j in range(0, 10):
		digcount.append(str(cube).count(str(j)))
	cubes[i]=digcount
	if cubes.count(digcount) == 5: print cubes.index(digcount), i, int(cubes.index(digcount)**3)
