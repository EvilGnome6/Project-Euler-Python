#NOTE: This problem is a more challenging version of Problem 81.

#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

#131 673 234 103 18
#201  96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524  37 331
	
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

rows = 5 #80
matrix = []
file = open("matrix.txt")

for i in range(rows):
	line = file.readline()
	row = map(int, line.split(','))
	matrix.append(row)

file.close()

matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

for row in matrix: print row

visited = [[0]*rows]*rows
completed = [[0]*rows]*rows

for row in visited: print row

#start at the left column to find the smallest cost entry point

print min(matrix)