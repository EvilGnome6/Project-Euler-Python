#-*- encoding: utf-8 -*-
#The square root of 2 can be written as an infinite continued fraction.

#The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

#It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.

#Hence the sequence of the first ten convergents for √2 are:
#1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

#What is most surprising is that the important mathematical constant,
#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

#The first ten terms in the sequence of convergents for e are:
#2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

#The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

#Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

limit = 100
sequence = [[0,0,1],[0,1,0],[2,0,0]]

for i in range(1, limit):
	sequence.append([1,0,0])
	sequence.append([i*2,0,0])
	sequence.append([1,0,0])
	if len(sequence) == limit + 2: break

for i in range(2, limit+2):
	sequence[i][1] = (sequence[i][0] * sequence[i-1][1]) + sequence[i-2][1]
	sequence[i][2] = (sequence[i][0] * sequence[i-1][2]) + sequence[i-2][2]
	
#print sequence

digsum = 0
numestr = str(sequence[limit+1][1])
for digit in numestr:
	digsum += int(digit)
	
print numestr, digsum
