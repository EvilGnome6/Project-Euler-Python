# -*- encoding: utf-8 -*-
#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

#By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.

#Find the least value of M such that the number of solutions first exceeds one million.

target = 10**6
count = 0
l = 2

while count < target:
	l += 1
	for wh in range(3, (2*l)+1):
		p = (float(wh**2 + l**2))**0.5
		if p == int(p):
			if wh <=l: count += wh/2
			else: count += 1 + (l - (wh+1)/2)

print l


