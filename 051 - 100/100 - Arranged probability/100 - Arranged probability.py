# -*- encoding: utf-8 -*-
#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

from time import time
t = time()

# https://oeis.org/A011900
# a(n+1)=3*a(n)-1+(8*a(n)^2-8*a(n)+1)^0.5, a(1)=1

alist = [1]

for n in range(1, 18):
	a =  3*alist[n-1] - 1 + (8*(alist[n-1]**2) - 8*alist[n-1]+1)**0.5
	alist.append(a)
	if (2* a * (a-1))**0.5 > 10**12: 
		print int(a), time()-t
		break
	