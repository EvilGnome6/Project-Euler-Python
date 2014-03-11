#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

num = 1

def getwnumones(num):
	if num == 1: return "one"
	if num == 2: return "two"
	if num == 3: return "three"
	if num == 4: return "four"
	if num == 5: return "five"
	if num == 6: return "six"
	if num == 7: return "seven"
	if num == 8: return "eight"
	if num == 9: return "nine"

def getwnumteens(num):
	if num == 10: return "ten"
	if num == 11: return "eleven"
	if num == 12: return "twelve"
	if num == 13: return "thirteen"
	if num == 14: return "fourteen"
	if num == 15: return "fifteen"
	if num == 16: return "sixteen"
	if num == 17: return "seventeen"
	if num == 18: return "eighteen"
	if num == 19: return "nineteen"
		
def getwnumtens(num):
	if num == 20: return "twenty"
	if num > 20 and num < 30: return ("twenty " + getwnums(num-20))
	if num == 30: return "thirty"
	if num > 30 and num < 40: return ("thirty " + getwnums(num-30))
	if num == 40: return "forty"
	if num > 40 and num < 50: return ("forty " + getwnums(num-40))
	if num == 50: return "fifty"
	if num > 50 and num < 60: return ("fifty " + getwnums(num-50))
	if num == 60: return "sixty"
	if num > 60 and num < 70: return ("sixty " + getwnums(num-60))
	if num == 70: return "seventy"
	if num > 70 and num < 80: return ("seventy " + getwnums(num-70))
	if num == 80: return "eighty"
	if num > 80 and num < 90: return ("eighty " + getwnums(num-80))
	if num == 90: return "ninety"
	if num > 90 and num < 100: 	return ("ninety " + getwnums(num-90))

def getwnumhuns(num):
	if num % 100 == 0: return(getwnums(num/100) + " hundred")
	else: return(getwnums(int(num/100)) + " hundred and " + getwnums(num-int(num/100)*100))

def getwnums(num):
	if num < 10:
		return(getwnumones(num))
	if num >= 10 and num < 20:
		return(getwnumteens(num))
	if num >= 20 and num < 100:
		return(getwnumtens(num))
	if num >= 100 and num < 1000:
		return(getwnumhuns(num))
	if num == 1000: return("one thousand")

sumlets = 0	

while num in range(1, 1001):
	wnum = getwnums(num)
	lets = (sum(c != ' ' for c in wnum))
	print(str(num) + " " + str(wnum) + " (" + str(lets) + " letters)")
	sumlets = sumlets + lets
	num += 1

print(sumlets)
