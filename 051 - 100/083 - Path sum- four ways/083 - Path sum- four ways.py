#NOTE: This problem is a significantly more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

#131 673 234 103 18
#201  96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524  37 331
	
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

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

#start at the top left node

visited[(0,0)] = matrix[0][0]
	
while True:

	#find the lowest value node, add it to completed and remove it from visited

	node = min(visited.items(), key=lambda x: x[1])
	completed[node[0]] = node[1]
	del visited[node[0]]

	#find neighboring nodes (up/down/left/right).
	
	neighbors = dict()

	if node[0][0] > 0: neighbors[(node[0][0]-1,node[0][1])] = 0 #up
	if node[0][0] < rows-1: neighbors[(node[0][0]+1,node[0][1])] = 0 #down
	if node[0][1] > 0: neighbors[(node[0][0],node[0][1]-1)] = 0 #left
	if node[0][1] < rows-1: neighbors[(node[0][0],node[0][1]+1)] = 0 #right

	#sum path to neighbors and add sum to visited if sum is lower.

	for nnode in neighbors:
		if nnode not in completed:
			if nnode not in visited:
				visited[nnode] = node[1] + matrix[nnode[0]][nnode[1]]
			else:
				if visited[nnode] < node[1] + matrix[nnode[0]][nnode[1]]:
					visited[nnode] < node[1] + matrix[nnode[0]][nnode[1]]
	if len(visited) == 0: break

#the value for the bottom right node in completed is the lowest cost route

print completed[(rows-1),(rows-1)]