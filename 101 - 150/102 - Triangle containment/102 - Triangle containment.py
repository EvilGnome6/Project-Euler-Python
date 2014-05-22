#-*- encoding:utf-8 -*-
#Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

#Consider the following two triangles:

#A(-340,495), B(-153,-910), C(835,-947)

#X(-175,41), Y(-421,-714), Z(574,-645)

#It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

#Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

#NOTE: The first two examples in the file represent the triangles in the example given above.

triangles = []
file = open("triangles.txt")

for i in range(1000):
	line = file.readline()
	line = line.strip()
	points = line.split(',')
	pointa, pointb, pointc = [int(points[0]),int(points[1])], [int(points[2]),int(points[3])], [int(points[4]),int(points[5])]
	triangles.append([pointa, pointb, pointc])

def getslope(a,b):
	if (float(b[0])-a[0]) == 0: return 100000
	return (float(b[1])-a[1])/(float(b[0])-a[0])

def getyint(a,b):
	m = getslope(a,b)
	return a[1]-(m*a[0])

def getxint(a,b):
	m = getslope(a,b)
	if m == 0: m = 0.00001
	b = getyint(a,b)
	return (-b/m)

def getxminmax(a,b):
	xmin, xmax = min(a[0], b[0]), max(a[0], b[0])
	return (xmin,xmax)
	
def getyminmax(a,b):
	ymin, ymax = min(a[1], b[1]), max(a[1], b[1])
	return (ymin,ymax)
	
def containsorigin(a, b, c):
	north, south, east, west = False, False, False, False
	
	abxint, abyint = [getxint(a,b),0], [0,getyint(a,b)]
	acxint, acyint = [getxint(a,c),0], [0,getyint(a,c)]
	bcxint, bcyint = [getxint(b,c),0], [0,getyint(b,c)]
	
	boundquad = []
	
	xminmax = getxminmax(a,b)
	if abxint[0] >= xminmax[0] and abxint[0] <= xminmax[1]: boundquad.append(abxint)
	yminmax = getyminmax(a,b)
	if abyint[1] >= yminmax[0] and abyint[1] <= yminmax[1]: boundquad.append(abyint)
	
	xminmax = getxminmax(a,c)
	if acxint[0] >= xminmax[0] and acxint[0] <= xminmax[1]: boundquad.append(acxint)
	yminmax = getyminmax(a,c)
	if acyint[1] >= yminmax[0] and acyint[1] <= yminmax[1]: boundquad.append(acyint)
	
	xminmax = getxminmax(b,c)
	if bcxint[0] >= xminmax[0] and bcxint[0] <= xminmax[1]: boundquad.append(bcxint)
	yminmax = getyminmax(b,c)
	if bcyint[1] >= yminmax[0] and bcyint[1] <= yminmax[1]: boundquad.append(bcyint)

	for intercept in boundquad:
		if intercept[0] == 0 and intercept[1] > 0: north = True
		elif intercept[0] == 0 and intercept[1] < 0: south = True
		elif intercept[0] > 0 and intercept[1] == 0: east = True
		elif intercept[0] < 0 and intercept[1] == 0: west = True
	if north == True and south == True and east == True and west == True: return True
	else: return False
	
count = 0
for triangle in triangles:
	a, b, c = triangle[0], triangle[1], triangle[2]
	if containsorigin(a,b,c) == True:
		count += 1
print count
