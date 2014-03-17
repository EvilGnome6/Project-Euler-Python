# -*- encoding: utf-8 -*-
#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

wordsfile = open('words.txt')
wordsstring = wordsfile.read()
wordsfile.close()
wordsstring = wordsstring.replace('\"', '')
words = wordsstring.split(',')

trinums = []
for n in range(1, 21):
	trinums.append((n*(n+1))/2)

def getvalue(word):
	value = 0
	for char in word:
		value += ord(char)-64
	return value

twords = 0
for word in words:
	if getvalue(word) in trinums:
		twords += 1
		
print twords