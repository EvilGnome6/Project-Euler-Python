#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

limit = 1000000
palsum = 0

for i in range(1, limit):
	if str(i) == (str(i)[::-1]):
		if (str(bin(i))[2::]) == (str(bin(i))[:1:-1]):
			palsum += i
			print i, str(bin(i))[2::], palsum

		
