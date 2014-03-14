#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4

#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

exp = 5
sumpowers = []

for i in range(2, 1000000):
	total = i
	d6 = int(total/100000)
	total = total-(d6*100000)
	d5 = int(total/10000)
	total = total-(d5*10000)
	d4 = int(total/1000)
	total = total-(d4*1000)
	d3 = int(total/100)
	total = total-(d3*100)
	d2 = int(total/10) 
	d1 = total-(d2*10)
	if (d6**exp)+(d5**exp)+(d4**exp)+(d3**exp)+(d2**exp)+(d1**exp) == i:
		sumpowers.append(i)

print(sum(sumpowers), sumpowers)