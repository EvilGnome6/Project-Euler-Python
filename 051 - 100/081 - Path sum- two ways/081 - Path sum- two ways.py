#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

	
#131 673 234 103  18
#201  96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524  37 331
	

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

rows = 80
matrix = []
file = open("matrix.txt")

for i in range(rows):
	line = file.readline()
	row = map(int, line.split(','))
	matrix.append(row)

file.close()

#matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

rows = len(matrix)

#for row in matrix: print row
#print " "

#sum the path cost on the bottom row from right to left
#sum the path cost on the righ column from bottom to top

for i in range(rows-2, -1, -1):
	matrix[rows-1][i] += matrix[rows-1][i+1]
	matrix[i][rows-1] += matrix[i+1][rows-1]

#for row in matrix: print row
#print " "

#work up from second to last row, from right to left, choosing least cost path

for i in range(rows-2, -1, -1):
	for j in range(rows-2, -1, -1):
		matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1])

#for row in matrix: print row
#print " "

print matrix[0][0]