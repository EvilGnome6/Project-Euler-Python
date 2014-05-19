#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

#What is the largest square number formed by any member of such a pair?

#NOTE: All anagrams formed must be contained in the given text file.

from time import time
t = time()

# copy all the words in the words.txt file to a words list
words = []
file = open("words.txt")
words = file.readline()
words = words.replace('\"', "")
words = words.split(',')
words.sort(lambda y,x: cmp(len(x), len(y)))

# create a second list of words with the letters sorted
sortwords = []
for word in words:
	sortwords.append(''.join(sorted(word)))

# search through the sorted words looking for duplicates and add to matchwords.
matchwords = []
for i in range(len(sortwords)):
	word = sortwords[i]
	if sortwords.count(word) > 1:
		match = []
		for j, k in enumerate(sortwords):
		    if k == word:
		        match.append(words[j])
		if match not in matchwords: matchwords.append(match)

# function to return the length of an integer
from math import log10
def length(number):
	return int(log10(number))+1

# function to return a list of squares with a given number of digits
def getsquares(digits):
	squares = []
	for i in range(int((10**(digits-1))**0.5), int((10**digits)**0.5)):
		number = i**2
		if length(number) == digits:
			squares.append(number)
	squares.reverse()
	return squares

# function to test if a pair of anagrams can be mapped to a pair of square numbers
def testmatch(match1, match2):
	for square in squares:
		firstsquare = square
		charmap = [None]*10
		mapped = True
		matched = False
		for i in range(len(match1)-1, -1, -1):
			char = match1[i]
			index = square % 10
			square /= 10
			if charmap[index] == None:
				charmap[index] = char
			else: 
				mapped = False
				break
		if mapped == True: 
			secondsquare = 0
			for l in match2:
				secondsquare *= 10
				secondsquare += charmap.index(l)
			
			if secondsquare in squares: 
				return match1, match2, firstsquare, secondsquare

# loop through the list of matches to find the first pair that matches
for match in matchwords:
	match1, match2 = match[0], match[1]
	digits = len(match1)
	squares = getsquares(digits)
	matchtest = testmatch(match1, match2)
	if matchtest != None:
		print matchtest, time()-t
		break
