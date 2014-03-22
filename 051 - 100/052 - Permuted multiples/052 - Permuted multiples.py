#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def countdigits(number):
	numstring = str(number)
	counts = []
	for i in range(1, 10):
		counts.append(numstring.count(str(i)))
	return counts

#print countdigits(113)		

for i in range(100000, 200000):
	numcount = countdigits(i)
	for j in range(2, 7):
		testcount = i * j
		if countdigits(testcount) != numcount: break
		if j == 6: 
			print i
			break
	
