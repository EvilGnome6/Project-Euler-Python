# -*- encoding: utf-8 -*-
#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3) − 1
#36 = 3 * 4 * (2 + 1)

#Note that concatenations of the digits, like 12 + 34, are not allowed.

#Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

from itertools import permutations
import operator
from time import time
t = time()

def targtest(digits,targ):
	ops={ 0:operator.add, 1:operator.sub, 2:operator.mul, 3:operator.div }
	perms = list(permutations(digits))
	for p in perms:
		for i in range(4):
			func = ops[i]
			if i < 4: result = func(p[0], p[1])
			for j in range(4):
				func = ops[j]
				for k in range(4):
					func1 = ops[i]
					func2 = ops[j]
					func3 = ops[k]
					if func3(func2(func1(p[0], p[1]), p[2]), p[3]) == targ: return True # a+b+c+d
					if func3(func1(p[0],func2(p[1],p[2])), p[3]) == targ: return True #a+(b+c)+d
			
	return False

maxlen = 0
maxset = []

for a in range(1,10):
	for b in range(a+1, 10):
		for c in range(b+1, 10):
			for d in range(c+1, 10):
				digits = [float(a), float(b), float(c), float(d)]
				targ = 1
				while True:
					if targtest(digits, targ) == False:
						if maxlen < targ-1:
							maxlen = targ-1
							maxset = digits
						break
					targ += 1

print maxset, maxlen, time()-t
