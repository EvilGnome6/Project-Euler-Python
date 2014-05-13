#Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

#A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

#The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

#By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

from time import time

t = time()

def getpuzzle(n):
	file = open("sudoku.txt")
	puzzle = []
	if n < 10: n = '0' + str(n)
	else: n = str(n)
	grid = "Grid " + n
	while True:
		line = file.readline()
		if grid in line: break
	for i in range(9):
		row = []
		line = file.readline()
		for d in line:
			try: row.append(int(d))
			except: pass
		puzzle.append(row)
	file.close()
	return puzzle

def getrow(puzzle, r, c):
	return puzzle[r]
	
def getcol(puzzle, r, c):
	column = []
	for i in range(9): column.append(puzzle[i][c])
	return column

def getbox(puzzle, r, c):
	box = []
	if r < 3: rrange = [0,1,2]
	elif r < 6: rrange = [3,4,5]
	else: rrange = [6,7,8]
	if c < 3: crange = [0,1,2]
	elif c < 6: crange = [3,4,5]
	else: crange = [6,7,8]
	for i in range(3):
		for j in range(3):
			box.append(puzzle[rrange[i]][crange[j]])
	return box

# function to return the possible numbers
def getposs(puzzle):
	# create a grid with all numbers in each node
	poss = [[range(1,10) for i in range(9)] for j in range(9)]
	for r in range(9):
		for c in range(9):
			# blank out any node that is solved
			if puzzle[r][c] != 0: poss[r][c] = []
			else:
				# remove numbers that exist in that node's row, col or box
				row, col, box = getrow(puzzle, r, c), getcol(puzzle, r, c), getbox(puzzle, r, c)
				for p in range(1,10):
					if p in row or p in col or p in box:
						if p in poss[r][c]: poss[r][c].remove(p)
	return poss

# function to test if the puzzle is solved (no 0s in the grid)
def issolved(puzzle):
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == 0: return False
	return True

# function to fetch the next unsolved node
def getunsolved(puzzle):
	# fetch a grid of possible values and return the first one with the shortest length
	poss = getposs(puzzle)
	for i in range(1, 9):
		for r in range(9):
			for c in range(9):
				if len(poss[r][c]) == i: return (r, c, poss[r][c])

# main solver function
def solve(puzzle):
	# returns true if the puzzle is solved
	if issolved(puzzle) == True: return True
	else:
		# fetch the next unsolved node
		node = getunsolved(puzzle)
		# if there are no unsolved nodes, then this must be a dead end so return false
		if node == None: return False
		r, c, poss = node[0], node[1], node[2] 
		for p in poss:
			# set the value of the node to a possible number and recursively call the function again
			# if the path is not valid, set the node to zero and backtrack
			puzzle[r][c] = p
			if solve(puzzle) == True: return True
			else:
				puzzle[r][c] = 0
	return False

total = 0
for i in range(1, 51):
	puzzle = getpuzzle(i)
	solve(puzzle)
	number = str(puzzle[0][0]) + str(puzzle[0][1]) + str(puzzle[0][2])
	total += int(number)

print total, time() - t

#for row in puzzle: print row
