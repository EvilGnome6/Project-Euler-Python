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

def targtest(digits,targ):
	ops={0:operator.add, 1:operator.sub, 2:operator.mul, 3:operator.div }
	perms = list(permutations(digits))
	for p in perms:
		for i in range(4):
			func = ops[i]
			result = func(p[0], p[1])
			for j in range(4):
				func = ops[j]
				result = func(result,p[2])
				for k in range(4):
					func = ops[k]
					result = func(result,p[3])
					if result == targ: return True
	return False

digits = [1.0,2.0,3.0,4.0]
print targtest(digits,3)

