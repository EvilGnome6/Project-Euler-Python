#Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

#A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

#The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

#By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

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

def solve(puzzle):
	solved = 0
	
	poss = [[range(1,10) for i in range(9)] for j in range(9)]
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] != 0: poss[r][c] = []

	while True:
		solved = 0
		for r in range(9):
			for c in range(9):
				if puzzle[r][c] != 0: 
					poss[r][c] = []
					continue
				row = getrow(puzzle, r, c)
				col = getcol(puzzle, r, c)
				box = getbox(puzzle, r, c)
				for p in range(1,10):
					if p in row or p in col or p in box:
						if p in poss[r][c]: poss[r][c].remove(p)
				if len(poss[r][c]) == 1:
					puzzle[r][c] = poss[r][c][0]
					solved += 1
#					print poss, r, c, solved

		if solved == 0:
			for r in range(9):
				print poss[r]
			return puzzle

puzzle = getpuzzle(2)
for r in puzzle: print r
print

solve(puzzle)

for r in puzzle: print r
print