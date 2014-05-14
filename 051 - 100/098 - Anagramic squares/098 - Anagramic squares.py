#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

#What is the largest square number formed by any member of such a pair?

#NOTE: All anagrams formed must be contained in the given text file.

words = []
file = open("words.txt")
words = file.readline()
words = words.replace('\"', "")
words = words.split(',')
words.sort(lambda y,x: cmp(len(x), len(y)))


sortwords = []
for word in words:
	sortwords.append(''.join(sorted(word)))

matchwords = []
for i in range(len(sortwords)):
	word = sortwords[i]
	if sortwords.count(word) > 1:
		match = []
		for j, k in enumerate(sortwords):
		    if k == word:
		        match.append(words[j])
		if match not in matchwords: matchwords.append(match)
		
for match in matchwords: print match, words.index(match[0]), words.index(match[1])

from math import log10
def length(number):
	return int(log10(number))+1

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

squares = []
for i in range(10**1, 10**5):
	number = i**2
	if length(number) == 5:
		squares.append(number)
squares.reverse()

sortsquares = []
for i in range(len(squares)):
	i = squares[i]
	sortsquares.append(''.join(sorted(str(i))))

match1 = words[1042]
match2 = words[1047]

print testmatch(match1, match2)
