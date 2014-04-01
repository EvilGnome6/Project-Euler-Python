#-*- encoding: utf-8 -*-
#The first ten continued fraction representations of (irrational) square roots are:

#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5

#Exactly four continued fractions, for N ≤ 13, have an odd period.


def transform(sqroot):
	a = int(sqroot**0.5)
	if sqroot**0.5 == a: return 0
	list = []
	list.append(a)
	numea = 0 - a
	deno = 1
	
	while True:
		numea, deno = deno, numea
		numeb = deno * -1
		deno = sqroot - deno**2
		deno = deno / numea
		numea = numea / numea
		a = int((sqroot**0.5 + numeb)/deno)
		numeb = numeb - (a * deno)
		numea = numeb
		list.append(a)
		if numea == (list[0]) * -1 and deno == 1: break
	return len(list) - 1

oddperiod = 0

for i in range(10001):
	period = transform(i)
	if period % 2 != 0: oddperiod += 1

print oddperiod
		