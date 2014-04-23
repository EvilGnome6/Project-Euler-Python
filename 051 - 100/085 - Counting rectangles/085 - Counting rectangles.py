#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

def rect(gridx, gridy):
	return (gridx**2+gridx)*(gridy**2+gridy)/4

target = 2000000
mindiff = 2000000

for x in range(1, 100):
	for y in range(x, 100):
		rects = rect(x,y)
		diff = abs(rects-target)
		if diff < mindiff:
			mindiff = diff
			xsol, ysol = x, y
		if rects > target:
			break

print xsol, ysol, mindiff, xsol*ysol
