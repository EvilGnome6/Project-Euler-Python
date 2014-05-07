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
	
def getboxpos(r, c, p):
	if r >= 0 and r <= 2: r = 0
	elif r >= 3 and r<= 5: r = 3
	else: r = 6
	if c >= 0 and c <= 2: c = 0
	elif c >= 3 and c <= 5: c = 3
	else: c = 6
	if p >= 0 and p <= 2: br, bc = 0, p
	elif p >= 3 and p<= 5: br, bc = 1, p-3
	else: br, bc = 2, p-6
	r += br 
	c += bc
	return[r,c]

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
				#Look for naked singles
				puzrow = getrow(puzzle, r, c)
				puzcol = getcol(puzzle, r, c)
				puzbox = getbox(puzzle, r, c)
				for p in range(1,10):
					if p in puzrow or p in puzcol or p in puzbox:
						if p in poss[r][c]: poss[r][c].remove(p)
				if len(poss[r][c]) == 1:
					puzzle[r][c] = poss[r][c][0]
					poss[r][c] = []
					solved += 1
				
				#Look for hidden singles
				if solved == 0:
					posrow = getrow(poss, r, c)
					poscol = getcol(poss, r, c)
					posbox = getbox(poss, r, c)
					for n in range(1, 10):
						count = 0
						for b in posrow:
							if n in b and n not in puzrow: count += 1
						if count == 1:
							for i in range(9):
								if n in posrow[i]:
#									print r, i, posrow, n
									puzzle[r][i] = n
									poss[r][i] = []
									solved += 1
						count = 0
						for b in poscol:
							if n in b and n not in puzcol: count += 1
						if count == 1:
							for i in range(9):
								if n in poscol[i]:
#									print r, i, puzcol, n
									puzzle[i][c] = n
									poss[i][c] = []
									solved += 1
						
						count = 0
						for b in posbox:
							if n in b and n not in puzbox: count += 1
						if count == 1:
							for i in range(9):
								if n in posbox[i]: p = i
							pos = getboxpos(r, c, p)
							puzzle[pos[0]][pos[1]] = n
							poss[pos[0]][pos[1]] = []
							solved += 1
							
					#Look for naked pairs
					if solved == 0:
						
						pairlist = []
						pair = False
						for i in range(9):
							if len(posrow[i]) == 2: 
								if posrow[i] in pairlist:
									pairlist = posrow[i]
									pair = True
									break
								else: pairlist.append(posrow[i])
						if pair == True: 
							for n in pairlist:
								for i in range(9):
									if posrow[i] != pairlist and n in posrow[i]: posrow[i].remove(n)
						
						pairlist = []
						pair = False
						for i in range(9):
							if len(poscol[i]) == 2:
								if poscol[i] in pairlist:
									pairlist = poscol[i]
									pair = True
									break
								else: pairlist.append(poscol[i])
						if pair == True:
							for n in pairlist:
								for i in range(9):
									if poscol[i] != pairlist and n in poscol[i]: poscol[i].remove(n)
							
						pairlist = []
						pair = False
						for i in range(9):
							if len(posbox[i]) == 2:
								if posbox[i] in pairlist:
									pairlist = posbox[i]
									pair = True
									break
								else: pairlist.append(posbox[i])
						if pair == True:
							for n in pairlist:
								for i in range(9):
									if posbox[i] != pairlist and n in posbox[i]: posbox[i].remove(n)

					#look for hidden pairs
					rcount, ccount, bcount = 0, 0, 0
					rpair, cpair, bpair = [], [], []
					rmatch, cmatch, bmatch  = [], [], []
					if solved == 0:
						for i in range(1, 10):
							for j in range(i+1, 10):
								for k in range(9):
									if i in posrow[k] and j in posrow[k] and len(posrow[k]) != 2: 
										rcount, rpair = rcount+1, [i,j]
										rmatch.append(k)
									if count == 2 and rpair == [4,7]: print rpair, rmatch
									rmatch = []

#									for l in range(9):
#										if rcount == 2 and rpair[0] in posrow[l] and l not in rmatch: count = 0
	
		if solved == 0:
			for i in range(9):
				print poss[i]
#				print getcol(poss, 0, i)
#			for i in range(3):
#				for j in range(3):
#					print getbox(poss, i*3, j*3)
#			print getbox(puzzle, 3, 4)
#			print getbox(poss, 3, 4)
			return puzzle

puzzle = getpuzzle(6)
for r in puzzle: print r
print

solve(puzzle)

print
for r in puzzle: print r


