#Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

#However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

#NOTE: The first two lines in the file represent the numbers in the example given above.

# copy all the base/exponent pairs in the base_exp.txt file to a basexp list
basexp = []
file = open("base_exp.txt")

for i in range(1000):
	line = file.readline()
	line = line.strip()
	pair = line.split(',')
	basexp.append([int(pair[0]),int(pair[1]), i+1])

# run through the list of pairs and track which is the largest.
from math import log10
maxpair = [1,1,0]
for pair in basexp:
	if log10(pair[0])*pair[1] > log10(maxpair[0])*maxpair[1]: maxpair = pair
print maxpair
