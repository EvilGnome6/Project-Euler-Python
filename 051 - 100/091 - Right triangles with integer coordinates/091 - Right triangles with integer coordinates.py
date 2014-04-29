# -*- encoding: utf-8 -*-
#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x1, y1, x2, y2 ≤ 2.

#Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

limit = 50
solutions = set()

for x1 in range(limit+1):
	for y1 in range(limit+1):
		for x2 in range(x1, limit+1):
			for y2 in range(limit+1):
				
				op = ((x1**2)+(y1**2))
				oq = ((x2**2)+(y2**2))
				pq = (((x2-x1)**2)+((y2-y1)**2))
				if op*oq*pq == 0: continue			
				hyp = max(op, oq, pq)
				if hyp == op: a, b = oq, pq
				elif hyp == oq: a, b = pq, op
				else: a, b = op, oq
				
				if hyp == a+b:
					if (x1,y1) < (x2,y2): p1p2 = (x1,y1,x2,y2)
					else: p1p2 = (x2,y2,x1,y1)
					solutions.add(p1p2)

print len(solutions)
