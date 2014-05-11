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
	
def isvalid(puzzle, r, c):
	row = getrow(puzzle, r, c)
	col = getcol(puzzle, r, c)
	box = getbox(puzzle, r, c)
	if row.count(puzzle[r][c]) > 1: return False
	if col.count(puzzle[r][c]) > 1: return False
	if box.count(puzzle[r][c]) > 1: return False
	return True
	
def solve(puzzle):
	# make a list of unknown squares
	unknown = []
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == 0: unknown.append((r,c))
	# step through the unknown squares. Increment by one and if valid, step to the next. If greater than 9, set to zero and jump back a step.
	i = 0
	while i < (len(unknown)):
		r, c = unknown[i][0], unknown[i][1]
		puzzle[r][c] += 1
		if puzzle[r][c] > 9:
			puzzle[r][c] = 0
			i -= 1
		elif isvalid(puzzle, r, c) == True: i += 1

total = 0
for i in range(1, 1):
	puzzle = getpuzzle(i)
	solve(puzzle)
	number = str(puzzle[0][0]) + str(puzzle[0][1]) + str(puzzle[0][2])
	total += int(number)

print total, time() - t

puzzle = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]

solve(puzzle)

for row in puzzle: print row