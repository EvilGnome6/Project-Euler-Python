#The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

#For example, the following represent all of the legitimate ways of writing the number sixteen:

#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI

#The last example being considered the most efficient, as it uses the least number of numerals.

#The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

#Find the number of characters saved by writing each of these in their minimal form.

#Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

denoms = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

rows = 1000
rnums = []
file = open("roman.txt")

for i in range(rows):
	line = file.readline()
	line = line.rstrip()
	rnums.append(line)

file.close()

def rtod(rnum):
	dnum = 0
	lastd = 1000
	for digit in rnum:
		d = denoms[digit]
		if d > lastd: dnum -= (2*lastd)
		dnum += d
		lastd = d
	return dnum

def dtor(dnum):
	rnum = ''

	while dnum - 1000 >= 0:
		rnum += 'M'
		dnum -= 1000

	if dnum - 900 >= 0:
		rnum += 'CM'
		dnum -= 900	

	while dnum - 500 >= 0:
		rnum += 'D'
		dnum -= 500

	if dnum - 400 >= 0:
		rnum += 'CD'
		dnum -= 400

	while dnum - 100 >= 0:
		rnum += 'C'
		dnum -= 100

	if dnum - 90 >= 0:
		rnum += 'XC'
		dnum -= 90

	while dnum - 50 >= 0:
		rnum += 'L'
		dnum -= 50

	if dnum - 40 >= 0:
		rnum += 'XL'
		dnum -= 40

	while dnum - 10 >= 0:
		rnum += 'X'
		dnum -= 10

	if dnum - 9 >= 0:
		rnum += 'IX'
		dnum -= 9

	while dnum - 5 >= 0:
		rnum += 'V'
		dnum -= 5

	if dnum - 4 >= 0:
		rnum += 'IV'
		dnum -= 4
	
	while dnum - 1 >= 0:
		rnum += 'I'
		dnum -= 1

	return rnum

counter = 0
	
for rnum in rnums: 
	dnum = rtod(rnum)
	mrnum = dtor(dnum)
	counter += len(rnum) - len(mrnum)

print counter

	

	