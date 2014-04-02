#Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

#Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

#It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#Total	Solution Set
#9	4,2,3; 5,3,1; 6,1,2
#9	4,3,2; 6,2,1; 5,1,3
#10	2,3,5; 4,5,1; 6,1,3
#10	2,5,3; 6,3,1; 4,1,5
#11	1,4,6; 3,6,2; 5,2,4
#11	1,6,4; 5,4,2; 3,2,6
#12	1,5,6; 2,6,4; 3,4,5
#12	1,6,5; 3,5,4; 2,4,6

#By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

#Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

import itertools

perms = list(itertools.permutations([1,2,3,4,5,6,7,8,9,10]))
perms.reverse()

def getsolset(perm):
	solset = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	solset[0][0] = perm[0]
	solset[0][1] = perm[1]
	solset[0][2] = perm[2]
	solset[1][0] = perm[3]
	solset[1][1] = perm[2]
	solset[1][2] = perm[4]
	solset[2][0] = perm[5]
	solset[2][1] = perm[4]
	solset[2][2] = perm[6]
	solset[3][0] = perm[7]
	solset[3][1] = perm[6]
	solset[3][2] = perm[8]
	solset[4][0] = perm[9]
	solset[4][1] = perm[8]
	solset[4][2] = perm[1]
	return solset

for perm in perms:
	solset = getsolset(perm)
	for set in solset: 	
		if set[0] < solset[0][0]: break
	else:
		for set in solset:
			if sum(set) != sum(solset[0]): break
		else:
			solstring = ""
			for i in solset:
				for j in i:
					solstring += str(j)
			print solset, solstring
			break
