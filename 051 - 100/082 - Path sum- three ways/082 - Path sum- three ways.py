#NOTE: This problem is a more challenging version of Problem 81.

#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

#131 673 234 103 18
#201  96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524  37 331
	
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

rows = 80
matrix = []
file = open("matrix.txt")

for i in range(rows):
	line = file.readline()
	row = map(int, line.split(','))
	matrix.append(row)

file.close()

#matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

visited = dict()
completed = dict()

#start at the left column add all the nodes to visited

for i in range(rows):
	node = (i,0)
	visited[node] = matrix[i][0]
	
while True:

	#find the lowest value node, add it to completed and remove it from visited

	node = min(visited.items(), key=lambda x: x[1])
	completed[node[0]] = node[1]
	del visited[node[0]]

	#find neighboring nodes (up/down/right).

	neighbors = dict()

	if node[0][0] > 0: neighbors[(node[0][0]-1,node[0][1])] = 0
	if node[0][0] < rows-1: neighbors[(node[0][0]+1,node[0][1])] = 0
	if node[0][1] < rows-1: neighbors[(node[0][0],node[0][1]+1)] = 0

	#sum path to neighbors and add sum to visited if sum is lower.

	for nnode in neighbors:
		if nnode not in completed:
			if nnode not in visited:
				visited[nnode] = node[1] + matrix[nnode[0]][nnode[1]]
			else:
				if visited[nnode] < node[1] + matrix[nnode[0]][nnode[1]]:
					visited[nnode] < node[1] + matrix[nnode[0]][nnode[1]]
	if len(visited) == 0: break

#collect the values on the right column from completed and print the minimum.

rcolumn = []
for node in completed:
	if node[1] == rows-1: rcolumn.append(completed[node])
print min(rcolumn)

